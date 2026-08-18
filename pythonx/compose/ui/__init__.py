"""`pythonx/compose/ui/__init__.py` -- the 2024 `from .modifier import Modifier` wrapper, unexecuted, and why.

## What used to be here, and why it never ran

A `try...except` block executing `from .modifier import Modifier`, `modifier = Modifier()`, and
`from .alignment import Alignment, AbsoluteAlignment`. `alignment.py` depended on `from java import jclass`
(Chaquopy-era JVM class lookup, retired in this codebase).

Furthermore, the relative import `from .modifier import Modifier` cannot resolve when `pythonx.compose` is registered.

## How `pythonx.compose.ui` actually resolves

Under the `PythonxAdapter` adaptation layer (`PythonMultiplatform`),
`register_package('pythonx.compose', 'androidx.compose')` registers `pythonx.compose` as a synthetic package
with `__path__ = []`.

When an application executes `import pythonx.compose.ui`, the adapter's import finder intercepts the request
and returns a synthetic module backed by `androidx.compose.ui` directly from `sys.modules`. The `Modifier` proxy
class is dynamically provided as `pythonx._proxy_type('androidx.compose.ui.Modifier')`.

As a result:
1. `import pythonx.compose.ui` never reads or executes this `__init__.py` file on disk.
2. If this file is loaded directly by path using `importlib`, the relative import `from .modifier import Modifier`
   fails with `ModuleNotFoundError: No module named 'pythonx.compose.ui.modifier'` because `pythonx.compose` has `__path__ = []`.

`modifier.py` works around this by being loaded out of band by path (`importlib.util.spec_from_file_location`),
never as `pythonx.compose.ui.modifier`. See `pythonx/compose/ui/modifier.py` and `pythonx/compose/runtime/__init__.py`
for the complete design rationale.
"""

from __future__ import annotations
