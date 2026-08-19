"""`pythonx/compose/wrapper/__init__.py` -- 2024 `KotlinWrapper` class mutation trick, retired.

## What used to be here, and why it is gone

`KotlinWrapper` reclassed live Java objects onto a Python class (`kotlin_object.__class__ = cls`).
That trick was Chaquopy-specific.

Under `PythonMultiplatform`, Kotlin objects are represented as `ObjectReference` integer handles in a
`HandleTable`, and an `int` does not support `__class__` assignment. Proxy classes and method attachment
are now handled by `PythonxAdapter`.
"""
