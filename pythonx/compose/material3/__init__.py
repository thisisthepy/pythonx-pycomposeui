# Theming
from .material_theming import *
from .color_scheme import *
from .dynamic_color import *
from .typography import *
from .shape import *

# Components
from .badge import *
from .bottom_app_bar import *
from .bottom_sheet import *
from .buttons import *
from .cards import *
from .checkbox import *
from .date_picker import *
from .dialogs import *
from .dividers import *
from .extended_fab import *
from .fab import *
from .icon_button import *
from .lists import *
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
