# Theming
from .color_scheme import *
from .dynamic_color import *
from .typography import *
from .shape import *

# Components
from .bottom_app_bar import *
from .bottom_sheet import *
from .checkbox import *
from .date_picker import *
from .dialogs import *
from .dividers import *
from .extended_fab import *
from .fab import *
from .menus import *
from .navigation_bar import *
from .navigation_drawer import *
from .navigation_rail import *
from .progress_indicators import *
from .radio_button import *
from .search_bar import *
from .segmented_button import *
from .sliders import *
from .snackbars import *
from .swipe_to_dismiss import *
from .switch import *
from .tabs import *
from .text_field import *
from .time_picker import *
from .tool_tip import *
from .top_app_bar import *

# Surfaces and layout
from .surfaces import *
from .scaffold import *

# Icons
from .icon import *

# `Text` is not here. `pythonx.compose.material3.Text` is a walked declaration -- the adaptation
# layer builds it from the artefact table, the same way `pythonx.compose.ui.Modifier.padding` is
# built and not hand-written (`pythonx/compose/ui/modifier.py`). A per-declaration `text.py` used to
# be imported here; it duplicated what the layer already does and could not be repaired (it looked
# `Text-<mangled>` up by a name-prefix search Kotlin's value-class mangling makes impossible -- see
# `modifier.py`'s module docstring for why). `tests/test_material3_module.py` is what checks this.
#
# `Button`, `Card`, `ListItem`, `Badge`/`BadgedBox` and `MaterialTheme` are not here either, for the
# same reason and on the same evidence shape: `PythonMultiplatform` commit `a6742a1c`
# (`ComposableRenderTest.kt`) renders each of them from Python with no wrapper at all, content
# lambda and (where present) `on_click` included, against the real `material3` jar --
#
#   buttonComposesItsClickHandlerAndItsRowScopedContent    -> buttons.py            (Button et al.)
#   cardResolvesToTheNonClickableOverloadAndDrawsItsContent -> cards.py             (Card et al.)
#   listItemComposesItsHeadlineContentUnderItsSnakeCasedName -> lists.py            (ListItem)
#   badgeDrawsItsLeafFormWithNoArgumentsAndMoreWithContent  -> badge.py             (Badge)
#   badgedBoxComposesBothItsBadgeAndItsContentScopes        -> badge.py             (BadgedBox)
#   materialThemeComposesAZeroArgumentContentLambda         -> material_theming.py  (MaterialTheme)
#
# Each of those files was a copy of the same `__COMPILED_CODE__` / `find_composable` /
# `name.startswith("<Name>-")` template `text.py` and `modifier.py` used -- the sibling declarations
# in each file (`ElevatedButton`, `OutlinedCard`, ...) were never individually rendered, but they are
# the identical template with only the `*Kt` attribute name changed, so the one proof per file is the
# same class of evidence the `Text` deletion already established: the template is dead, not the
# specific name. `tests/test_material3_module.py` asserts each file is gone.
#
# `icon_button.py` is now gone entirely, not just half. `IconButton` and its plain siblings already
# had the render proof (`iconButtonComposesItsClickHandlerAndItsContent`, `a6742a1c`). The
# `IconToggleButton` family (`checked: Boolean`, `onCheckedChange: (Boolean) -> Unit`) needed a
# different shape of proof -- a static render delivers no events, so nothing about a callback slot
# could be shown by rasterising -- and `PythonMultiplatform` commit `3fde8bd6`
# (`CallbackDrivenRenderTest.kt`) supplies it: a real pointer press and release through
# `ImageComposeScene.sendPointerEvent`, asserted to invoke the Python callback with the value Compose
# handed it, on **two** declarations deliberately (`Checkbox` in `CheckboxKt`, then `Switch` in
# `SwitchKt`, specifically to rule out a mechanism that only happens to work for one file). The
# `IconToggleButton` family is a third declaration, in a third file (`IconButtonKt`), with that exact
# same `(Boolean) -> Unit` shape -- the same class of generalisation this module already applies
# within a single file for `Button`'s and `IconButton`'s untested siblings, extended here across
# files because the render test itself was built to cross that boundary.
#
# `text_field.py`'s `TextField`/`OutlinedTextField` do **not** get the same conclusion.
# `on_value_change` is `(String) -> Unit` -- a shape `CallbackDrivenRenderTest.kt` never drives, only
# `(Boolean) -> Unit` -- so the slot is bound (checked, not assumed: `ComposableBindingTest.kt:392`)
# but not proven end to end, and `text_field.py` stays hand-written until a render test drives a
# `String`-valued callback the same way. `tests/test_material3_module.py` is what checks all of this.
#
# `checkbox.py` and `switch.py` are not files in the sense any of the above are: both have been
# empty since before this package had an adaptation layer to defer to (`git log -p` on either shows
# no non-empty version). `Checkbox`/`Switch` reach Python entirely through the walked table -- which
# is exactly what `CallbackDrivenRenderTest.kt` exercises above -- and the empty files cost nothing
# and assert nothing; they are left as they are rather than deleted, so as not to conflate "always
# empty" with "emptied on evidence" in the file history.
