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

`Button`, `Card`, `ListItem`, `Badge`/`BadgedBox`, `MaterialTheme` and (half of) `IconButton` are the
same shape again, on `PythonMultiplatform` commit `a6742a1c` (`ComposableRenderTest.kt`): each renders
from Python with no wrapper, content lambda and `on_click` included where the declaration has one.
`IconToggleButton` and its siblings, and `text_field.py`'s `TextField`/`OutlinedTextField`, are
deliberately *not* asserted dead here even though their slot types are confirmed bound
(`ComposableBindingTest.kt:392`, `Checkbox.onCheckedChange` resolves to
`kotlin.Function1(kotlin.Boolean)->kotlin.Unit`): no render test drives their callback, and
`ComposableRenderTest.kt` states directly that a static render delivers no events, so that proof
needs a different shape than the ink comparison `Button`/`IconButton` got. See
`pythonx/compose/material3/__init__.py`'s trailing comment and `icon_button.py`'s module docstring
for the full citations.
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


class TheRenderProvenWrappersAreGone(unittest.TestCase):
    """Each of these files was the same `text.py`/`modifier.py` template: `__COMPILED_CODE__`,
    `find_composable`, and a `name.startswith("<Name>-")` mangled-suffix search over `*Kt.__dict__`.
    `PythonMultiplatform` commit `a6742a1c` (`ComposableRenderTest.kt`) rendered one declaration per
    file from Python with no wrapper at all, which is the same evidence `Text` had -- so the whole
    file goes, the same way `text.py` did.
    """

    # module filename -> (render test that proved it, declaration(s) it proves)
    PROVEN_FILES = {
        "buttons.py": (
            "buttonComposesItsClickHandlerAndItsRowScopedContent", "Button"
        ),
        "cards.py": (
            "cardResolvesToTheNonClickableOverloadAndDrawsItsContent", "Card"
        ),
        "lists.py": (
            "listItemComposesItsHeadlineContentUnderItsSnakeCasedName", "ListItem"
        ),
        "badge.py": (
            "badgeDrawsItsLeafFormWithNoArgumentsAndMoreWithContent / "
            "badgedBoxComposesBothItsBadgeAndItsContentScopes", "Badge, BadgedBox"
        ),
        "material_theming.py": (
            "materialThemeComposesAZeroArgumentContentLambda", "MaterialTheme"
        ),
    }

    def test_proven_wrapper_files_do_not_exist(self):
        for filename, (test_name, decl) in self.PROVEN_FILES.items():
            self.assertFalse(
                (MATERIAL3_DIR / filename).exists(),
                f"{filename} wraps {decl}, which {test_name} already proves the adaptation layer "
                "renders with no Python wrapper (PythonMultiplatform commit a6742a1c)",
            )

    def test_material3_package_does_not_import_the_deleted_modules(self):
        source = MATERIAL3_INIT.read_text(encoding="utf-8")
        for filename in self.PROVEN_FILES:
            module = filename[:-3]  # strip ".py"
            self.assertNotIn(
                f"from .{module} import", source,
                f"__init__.py still imports the deleted {filename}",
            )


class IconButtonIsOnlyHalfGone(unittest.TestCase):
    """`IconButton` has the same render proof as `Button` (`iconButtonComposesItsClickHandlerAndIts
    Content`), and `FilledIconButton`/`FilledTonalIconButton`/`OutlinedIconButton` are the identical
    template. The toggle variants stay: their `on_checked_change` slot type is confirmed *bound*
    (`ComposableBindingTest.kt:392`), but no render test drives the callback -- see the module
    docstring for why a static render cannot prove that the way it proved `on_click`.
    """

    def setUp(self):
        self.source = (MATERIAL3_DIR / "icon_button.py").read_text(encoding="utf-8")

    def test_the_four_render_proven_classes_are_gone(self):
        for banned in ("class IconButton(", "class FilledIconButton(",
                       "class FilledTonalIconButton(", "class OutlinedIconButton("):
            self.assertNotIn(
                banned, self.source,
                f"{banned} is the same render-proven template Button's deletion already covers "
                "(iconButtonComposesItsClickHandlerAndItsContent, commit a6742a1c)",
            )

    def test_the_toggle_variants_are_still_here(self):
        # Not proven render-reachable yet (no test drives on_checked_change from a rendered frame),
        # so removing these would not be backed by the same evidence the plain variants have.
        for kept in ("class IconToggleButton(", "class FilledIconToggleButton(",
                     "class FilledTonalIconToggleButton(", "class OutlinedIconToggleButton("):
            self.assertIn(kept, self.source)

    def test_icon_button_module_is_still_imported(self):
        source = MATERIAL3_INIT.read_text(encoding="utf-8")
        self.assertIn("from .icon_button import", source)


class TextFieldIsUntouchedPendingARenderProof(unittest.TestCase):
    """`on_value_change` is `(String) -> Unit`, the same shape as `IconToggleButton`'s
    `on_checked_change` and the same open question: bound at the type level, not proven end to end.
    """

    def test_text_field_module_still_exists(self):
        self.assertTrue((MATERIAL3_DIR / "text_field.py").exists())

    def test_text_field_still_defines_its_two_classes(self):
        source = (MATERIAL3_DIR / "text_field.py").read_text(encoding="utf-8")
        self.assertIn("class TextField(", source)
        self.assertIn("class OutlinedTextField(", source)


if __name__ == "__main__":
    unittest.main()
