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
from .icon_button import *
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
# `icon_button.py` is only half gone. `IconButton` itself has the same proof
# (`iconButtonComposesItsClickHandlerAndItsContent`), and `FilledIconButton`/`FilledTonalIconButton`/
# `OutlinedIconButton` are the same template again -- all four are removed. `IconToggleButton` and
# its `Filled`/`FilledTonal`/`Outlined` siblings stay, and so does `text_field.py`'s
# `on_value_change` -- checked, not assumed: their `(Boolean) -> Unit` / `(String) -> Unit` slots
# *are* bound (`ComposableBindingTest.kt:392` resolves `Checkbox.onCheckedChange` to exactly
# `kotlin.Function1(kotlin.Boolean)->kotlin.Unit`, and that path predates `728809bc` -- it is
# composable-slot binding from `a179b747`, a different mechanism from the plain-function-parameter
# path `728809bc` actually opened). What is missing is the render proof: `ComposableRenderTest.kt`
# states directly that a static render delivers no events, so a callback-shaped slot like
# `onCheckedChange` cannot be shown to work by rasterising the way `IconButton`'s `on_click` was --
# no test renders `IconToggleButton`, `Checkbox`, `Switch`, `TextField` or `OutlinedTextField` from
# Python or drives their callback. Until that proof exists, in whatever shape it turns out to take,
# these stay hand-written.
