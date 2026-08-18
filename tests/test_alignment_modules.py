"""`alignment.py` / `arrangement.py` -- loadable now, and still unbound.

Both files carried Chaquopy-era code that could not run: `from java import jclass` at module
level, in a project whose bridge is not Chaquopy. Importing either one raised before a single
class body executed, so the "blocked upstream" note they carried described something nobody
could reach anyway.

Two things are asserted, and they are separate on purpose:

1. **They load.** Importing them by path no longer raises. That is what changed.
2. **They are still unbound.** No `jclass` survives in executable tokens, and the classes carry
   no constants -- because the artefact scanner binds top-level functions and value-class
   constructors, and `Alignment.Center` / `Arrangement.SpaceBetween` are neither. When that
   changes upstream, this test fails and these files get real contents.

Tokens are checked rather than raw text, so a mention inside the docstring that explains the
history does not count as surviving code -- the same distinction `test_ui_init_module.py` makes.
"""

from __future__ import annotations

import importlib.util
import io
import tokenize
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

MODULES = {
    "alignment": REPO / "pythonx" / "compose" / "ui" / "alignment.py",
    "arrangement": REPO / "pythonx" / "compose" / "layout" / "arrangement.py",
}


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(f"_pxc_probe_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _executable_names(path: Path) -> set[str]:
    with path.open("rb") as handle:
        return {
            token.string
            for token in tokenize.tokenize(handle.readline)
            if token.type == tokenize.NAME
        }


class BothModulesLoadWithoutChaquopy(unittest.TestCase):
    def test_importing_by_path_no_longer_raises(self) -> None:
        for name, path in MODULES.items():
            with self.subTest(module=name):
                self.assertTrue(path.exists(), f"{path} is missing")
                _load(name, path)

    def test_no_jclass_survives_in_executable_tokens(self) -> None:
        for name, path in MODULES.items():
            with self.subTest(module=name):
                self.assertNotIn(
                    "jclass",
                    _executable_names(path),
                    f"{name} still executes Chaquopy-era code",
                )


class TheLayerSuppliesThemNow(unittest.TestCase):
    """The canary this file used to carry has fired.

    It asserted that neither module exposed a constant, and said that the day the scanner learned to
    bind object constants it would fail and these files would get real contents. Upstream's
    `80318c16` taught it, `6d896fba` proved a constant crosses, so the placeholder classes are gone
    -- the layer produces the names and this package's rule is not to wrap what the layer produces.

    What stays asserted is what a caller cannot read off the layer: which names exist, and that they
    are called rather than read.
    """

    ALIGNMENT = (
        "Bottom", "BottomCenter", "BottomEnd", "BottomStart", "Center", "CenterEnd",
        "CenterHorizontally", "CenterStart", "CenterVertically", "End", "Start", "Top",
        "TopCenter", "TopEnd", "TopStart",
    )
    ARRANGEMENT = ("Bottom", "Center", "End", "SpaceAround", "SpaceBetween", "SpaceEvenly", "Start", "Top")

    def test_no_placeholder_classes_remain(self) -> None:
        for name, path in MODULES.items():
            with self.subTest(module=name):
                module = _load(name, path)
                classes = [
                    attribute
                    for attribute in vars(module).values()
                    if isinstance(attribute, type) and attribute.__module__ == module.__name__
                ]
                self.assertEqual([], classes, f"{name} still declares a placeholder the layer supplies")

    def test_each_module_names_the_constants_the_walker_binds(self) -> None:
        for name, expected in (("alignment", self.ALIGNMENT), ("arrangement", self.ARRANGEMENT)):
            doc = MODULES[name].read_text()
            for constant in expected:
                with self.subTest(module=name, constant=constant):
                    self.assertIn(constant, doc, f"{name} does not name {constant}")

    def test_each_module_says_the_constants_are_called(self) -> None:
        """Reading one without calling it passes the function object and the dispatcher refuses it."""
        for name, path in MODULES.items():
            with self.subTest(module=name):
                self.assertIn("()", path.read_text(), f"{name} does not show the call form")
                self.assertIn("parentheses", path.read_text(), f"{name} does not say why")


if __name__ == "__main__":
    unittest.main()
