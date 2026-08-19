"""`pythonx/compose/lite/app.py` -- 2024 JPype standalone prototype, retired.

## What used to be here, and why it is gone

A sample standalone script importing `jvm.init_jvm()`, `org.example.project.AppKt`, and hand-written
lite wrappers (`material3.Text`, `runtime.Composable`, `register_composer`).

This was part of an early 2024 JPype experiment before the architecture moved to `PythonxAdapter` and
direct Kotlin/Native & JVM upcalls via PythonMultiplatform FFI.

## Modern usage

Applications no longer initialize JPype or call `AppKt.launch()`. Instead, host integration via
`PythonxAdapter` handles binding and `@Composable` evaluation.
"""
