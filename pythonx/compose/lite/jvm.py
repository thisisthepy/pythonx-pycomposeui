"""`pythonx/compose/lite/jvm.py` -- 2024 JPype JVM launcher, retired.

## What used to be here, and why it is gone

`jpype.startJVM()` initialization script for loading `ComposeLite-1.0-all.jar` using JPype.

This repository no longer uses JPype for JVM lifecycle management. Interoperability is handled
natively by `PythonMultiplatform` FFI and upcall trampolines.
"""
