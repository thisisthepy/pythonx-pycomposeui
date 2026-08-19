"""`pythonx/compose/layout/__init__.py` -- layout definitions provided by the adaptation layer.

## What used to be here, and why it is gone

A try...except block executing relative import `from .arrangement import Arrangement`. `arrangement.py`
is a docstring module (no `Arrangement` class is declared inside it). Attempting to import `Arrangement`
from `.arrangement` raised `ImportError`.

## How `pythonx.compose.layout` / `pythonx.compose.foundation.layout` resolves

Under `PythonxAdapter` (`PythonMultiplatform`), layout components and arrangements
(`Arrangement`, `Column`, `Row`, `Spacer`, etc.) are generated dynamically from `androidx.compose.foundation.layout`
into `sys.modules`.

When an application executes `import pythonx.compose.foundation.layout` or accesses layout properties,
the adapter resolves declarations dynamically.

## Calling convention for constants

Constants on layout objects (e.g., `Arrangement.Start`, `Arrangement.Center`, `Arrangement.SpaceBetween`)
are accessed directly as properties **without parentheses** (`Arrangement.Start`, `TextStyle.Default`),
per the updated binding convention.
"""
