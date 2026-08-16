"""`pythonx/compose/material3/` -- which per-declaration wrappers the adaptation layer already covers.

`Text` is the one this asserts, and only this one: `docs/...` (`ComposableRenderTest.kt`,
`PythonMultiplatform` commit `c60bcfeb`) proved `from pythonx.compose.material3 import Text;
Text('hi')` draws real pixels through the walked `material3` jar with **no Python wrapper at all** --
the same shape `test_modifier_module.py` proved for `Modifier.padding`. `pythonx/compose/material3/
text.py` predates that: it imports `androidx.compose.material3.TextKt` directly (a mechanism this
tree no longer has) and, on the way in, does the exact `name.startswith("Text-")` mangled-suffix
search `test_modifier_module.TheShellIsGone` already bans for `Modifier` -- the same impossible
search, since Kotlin's value-class mangling suffix hashes the signature and not the name. It cannot
be repaired; it can only be removed, the way `modifier.py`'s copy of it was.

Nothing here proves Compose still renders `Text` -- that is `ComposableRenderTest.kt`'s job, in the
other repository, and it needs a JVM this repository does not have. What this checks is local: that
the dead wrapper is gone and nothing in this repository still points at it.

`Icon`, `ColorScheme`, `lightColorScheme` and `darkColorScheme` are the same shape (`TextKt` /
`IconKt` / `ColorSchemeKt` imports, the same mangled-suffix search) but nothing has independently
confirmed them walked and rendering the way `Text` is confirmed -- so they are left alone here rather
than asserted dead on architecture alone. `docs/` and the migration report list them as the same
class of finding, unconfirmed.
"""

from __future__ import annotations

import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MATERIAL3_DIR = REPO / "pythonx" / "compose" / "material3"
MATERIAL3_INIT = MATERIAL3_DIR / "__init__.py"


class TheTextWrapperIsGone(unittest.TestCase):
    """`Text` needs no Python: `pythonx.compose.material3.Text` is a walked declaration."""

    def test_text_module_does_not_exist(self):
        self.assertFalse(
            (MATERIAL3_DIR / "text.py").exists(),
            "text.py is a per-declaration wrapper the adaptation layer already covers "
            "(PythonMultiplatform commit c60bcfeb renders Text('hi') with none)",
        )

    def test_material3_package_does_not_import_a_text_module(self):
        # Substring, not `"text"` alone: `text_field.py` is a real, still-pending wrapper (`content=`
        # gated, `docs/` lists it under the components waiting on lambda content) and must stay
        # imported here. Only the exact `.text` submodule this test is about is banned.
        source = MATERIAL3_INIT.read_text(encoding="utf-8")
        self.assertNotIn("from .text import", source)


if __name__ == "__main__":
    unittest.main()
