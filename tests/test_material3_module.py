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

`icon_button.py` is now gone entirely. `PythonMultiplatform` commit `3fde8bd6`
(`CallbackDrivenRenderTest.kt`) is the render proof the previous version of this module's docstring
said was missing: it drives `Checkbox`'s `onCheckedChange` with a real pointer press and release
through `ImageComposeScene.sendPointerEvent` -- no window, no display -- and asserts the Python
callback ran with the value Compose handed it (`_cb_events == [True]`) and that a fresh render shows
the state it wrote. `theSameCallbackShapeIsDrivenOnASecondDeclaration` repeats it on `Switch`,
deliberately: a different file (`SwitchKt` vs `CheckboxKt`), a different declaration, the identical
`(Boolean) -> Unit` shape, written specifically to rule out "a lucky slot index that only happens to
work for `Checkbox`". `IconToggleButton`/`FilledIconToggleButton`/`FilledTonalIconToggleButton`/
`OutlinedIconToggleButton` are a *third* declaration (`IconButtonKt`, a third file again) with that
same shape and the same parameter names (`checked: Boolean`, `onCheckedChange: (Boolean) -> Unit`) --
the evidence the render test was built to generalise across declaration boundaries applies to them
for the same reason it already covers two unrelated files. So the four toggle classes are deleted the
same way `IconButton`'s plain siblings were.

`text_field.py`'s `TextField`/`OutlinedTextField` are the one case this does **not** reach.
`on_value_change` is `(String) -> Unit`, not `(Boolean) -> Unit` -- a different argument type that
`CallbackDrivenRenderTest.kt` never drives. The callback-shape generalisation above is about the
mechanism working across *declarations* with one proven *shape*; it says nothing about a shape that
was never exercised. So `text_field.py` stays hand-written, and it is missing exactly one thing: a
render test of the same family driving a `String`-valued callback (e.g. typing into a `TextField` and
reading the string a fresh render shows), which does not exist yet in either repository.

Nothing here proves Compose still renders `IconToggleButton` when it composes for real -- that
render-with-real-Compose claim is what `CallbackDrivenRenderTest.kt` supplies, in the other
repository, over `Checkbox` and `Switch` specifically. What this file checks is local: that the dead
wrapper is gone and nothing in this repository still points at it, the same thing it already checked
for `Text` and for `Button`'s siblings.
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


class TheIconButtonModuleIsEntirelyGone(unittest.TestCase):
    """`IconButton` and its plain siblings had the same render proof as `Button`
    (`iconButtonComposesItsClickHandlerAndItsContent`, commit `a6742a1c`) and were already deleted
    here. The toggle variants (`IconToggleButton`, `FilledIconToggleButton`,
    `FilledTonalIconToggleButton`, `OutlinedIconToggleButton`) are gone too now: `PythonMultiplatform`
    commit `3fde8bd6` (`CallbackDrivenRenderTest.kt`) proves the `(Boolean) -> Unit` callback shape
    they share with `Checkbox`/`Switch` is driven end to end by a real pointer event on two unrelated
    declarations, and the toggle buttons are a third declaration with the identical shape. With both
    halves proven, the whole file is redundant -- the same conclusion `text.py`'s deletion reached for
    a single declaration, reached here for all four.
    """

    def test_icon_button_module_does_not_exist(self):
        self.assertFalse(
            (MATERIAL3_DIR / "icon_button.py").exists(),
            "icon_button.py wrapped IconButton (already render-proven, a6742a1c) and the "
            "IconToggleButton family, whose (Boolean) -> Unit callback shape is now render-proven "
            "on two other declarations (3fde8bd6, CallbackDrivenRenderTest.kt)",
        )

    def test_material3_package_does_not_import_icon_button(self):
        source = MATERIAL3_INIT.read_text(encoding="utf-8")
        self.assertNotIn("from .icon_button import", source)


class TextFieldIsUntouchedPendingARenderProof(unittest.TestCase):
    """`on_value_change` is `(String) -> Unit` -- a callback *shape* `CallbackDrivenRenderTest.kt`
    never drives (it only exercises `(Boolean) -> Unit`, on `Checkbox` and `Switch`). The toggle
    buttons could lean on that test because they share its exact shape; `TextField` cannot, so it
    stays bound at the type level and unproven end to end until a render test drives a `String`
    callback the way `3fde8bd6` drives a `Boolean` one.
    """

    def test_text_field_module_still_exists(self):
        self.assertTrue((MATERIAL3_DIR / "text_field.py").exists())

    def test_text_field_still_defines_its_two_classes(self):
        source = (MATERIAL3_DIR / "text_field.py").read_text(encoding="utf-8")
        self.assertIn("class TextField(", source)
        self.assertIn("class OutlinedTextField(", source)


if __name__ == "__main__":
    unittest.main()
