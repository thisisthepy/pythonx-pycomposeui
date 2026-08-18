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


class NeitherIsBoundYet(unittest.TestCase):
    """When the scanner learns to bind object constants, this fails and the files get contents."""

    def test_the_classes_expose_no_constants(self) -> None:
        alignment = _load("alignment", MODULES["alignment"])
        arrangement = _load("arrangement", MODULES["arrangement"])
        for owner, attribute in (
            (alignment.Alignment, "Center"),
            (alignment.AbsoluteAlignment, "TopLeft"),
            (arrangement.Arrangement, "SpaceBetween"),
        ):
            with self.subTest(owner=owner.__name__, attribute=attribute):
                self.assertFalse(
                    hasattr(owner, attribute),
                    f"{owner.__name__}.{attribute} exists -- the scanner may now bind object "
                    f"constants, in which case these modules should carry real bindings",
                )


if __name__ == "__main__":
    unittest.main()
