"""`pythonx/compose/ui/__init__.py` -- testing that the on-disk file is unexecuted and dead.

Three things are asserted here:
1. That `import pythonx.compose.ui` under an installed adapter returns the synthetic module produced
   by `PythonxAdapter` (`register_package('pythonx.compose', 'androidx.compose')`), NOT the file on disk.
2. That the synthetic `pythonx.compose.ui` module exposes the `Modifier` proxy type directly.
3. That no dead Chaquopy-era code (`jclass`, `from .modifier import Modifier`, etc.) survives in
   executable tokens in `pythonx/compose/ui/__init__.py`.
"""

from __future__ import annotations

import importlib.util
import io
import sys
import tokenize
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import adapter as adapter_loader  # noqa: E402
import fake_host  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
UI_INIT_PY = REPO / "pythonx" / "compose" / "ui" / "__init__.py"


class TheUiInitModuleIsUnreachableAndDead(unittest.TestCase):
    """The claim `pythonx/compose/ui/__init__.py` makes about ordinary import and Chaquopy dead code."""

    def setUp(self):
        try:
            source = adapter_loader.read_adapter_source()
        except adapter_loader.AdapterUnavailable as unavailable:
            self.skipTest(str(unavailable))
        self.host = fake_host.FakeHost()
        self.host.bind()
        self.pythonx = adapter_loader.install(source)
        self.host.register(self.pythonx)
        self.addCleanup(self.host.unbind)
        self.addCleanup(adapter_loader.uninstall)

    def test_import_pythonx_compose_ui_returns_synthetic_adapter_module(self):
        import pythonx.compose.ui as ui

        # The synthetic module produced by PythonxAdapter has no __file__ attribute pointing to disk
        self.assertFalse(
            hasattr(ui, "__file__"),
            "import pythonx.compose.ui must return the synthetic module, not the on-disk file",
        )
        self.assertTrue(
            hasattr(ui, "Modifier"),
            "synthetic module must expose Modifier proxy type",
        )

    def test_on_disk_ui_init_is_not_imported_by_ordinary_import(self):
        import pythonx.compose.ui as ui

        # Verify that sys.modules['pythonx.compose.ui'] is not the on-disk __init__.py file
        loaded_file = getattr(ui, "__file__", None)
        self.assertNotEqual(
            loaded_file,
            str(UI_INIT_PY),
            "pythonx.compose.ui on disk must not be loaded by ordinary import",
        )


class TheChaquopyUiInitMechanismIsGone(unittest.TestCase):
    """No `jclass`, no relative imports `from .modifier import Modifier` in `ui/__init__.py`."""

    def setUp(self):
        raw = UI_INIT_PY.read_text(encoding="utf-8")
        kept = []
        for tok in tokenize.generate_tokens(io.StringIO(raw).readline):
            if tok.type in (tokenize.STRING, tokenize.COMMENT):
                continue
            kept.append(tok.string)
        self.tokens = set(kept)

    def test_no_chaquopy_or_relative_import_tokens_survive(self):
        for banned in ("jclass", "modifier", "alignment", "AbsoluteAlignment"):
            self.assertNotIn(
                banned,
                self.tokens,
                f"{banned} is dead Chaquopy-era code or invalid relative import in ui/__init__.py",
            )


if __name__ == "__main__":
    unittest.main()
