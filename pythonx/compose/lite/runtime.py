"""`pythonx/compose/lite/runtime.py` -- 2024 JPype runtime composer registry, retired.

## What used to be here, and why it is gone

A module-level `_composer` variable and `register_composer()` function used to pass a single JPype composer instance.

Composer management is now handled dynamically by `PythonComposition` and `pythonx._bind_composable`
during composition passes without needing a Python-side global composer registry.
"""
