"""`pythonx/compose/runtime/__init__.py` -- the 2024 `Composable` class, gone, and what is left.

## What used to be here, and why it never ran

A decorator class (`Composable`) holding one `__composer`, plus `ComposeApp`, `KotlinComposable`,
`KotlinWidget` and a `CoroutineScope` family, all built on `jclass` --
`_runtime = jclass("io.github.thisisthepy.pycomposeui.RuntimeKt")` -- chaquopy's name-based
Java/Kotlin class lookup. `jclass` was never imported in this module, in any commit where the module
had content (`git log -p` on this file shows no `import jclass` anywhere), so every one of those five
module-level statements raised `NameError` before a single class body executed:

    >>> from pythonx.compose.runtime import Composable
    NameError: name 'jclass' is not defined

That is not incidental breakage, it is a different technology than this repository now targets.
`jclass` is chaquopy's global; `PythonMultiplatform`'s binder is a different bridge
(`docs/pythonx-adapter-design.md` §5.1, in `PythonMultiplatform`, reads the same class as "the 2024
`Composable` class", and `agent-rules.md` §12 retires name-based JVM lookup by name). The other half
of what `Composable.__call__` did -- inspecting `self.compose.__code__.co_varnames` to find where
`content` sat, so it could be popped out and wrapped specially -- is retired for the same reason
`modifier.py`'s mangled-suffix search was: `docs/pythonx-adapter-design.md` §5.6/§7 record that
composer threading, `$changed` and `$default` are now arithmetic `pythonx._bind_composable` does from
a slot's *declared type*, uniformly, for a `content` lambda exactly as for any other parameter. There
is nothing left for a Python-side base class to detect or thread by hand.

## What is left

One identity decorator, `Composable`, kept because `UI.ipynb` writes `@Composable` on every
screen-defining function and that surface is one an application author should keep being able to
write. Nothing needs to happen to the decorated function for it to work: the composer any nested
`pythonx.compose.*` call needs comes from the one hand-written Kotlin `@Composable`
(`PythonComposition`, in `PythonMultiplatform`) pushing it once per composition pass, and from the
*callee's* slot type deciding whether and how to thread it -- never from anything the caller does.
A plain `def Screen(): Button(...)` already works with no wrapper, no base class and no `content=`
slot detection; `@Composable` changes nothing about that and exists only so the notebook's own
spelling keeps working.

## What this file cannot do

`pythonx.compose.runtime` -- this file's own dotted name -- is not reachable through
`import pythonx.compose.runtime` once `PythonxAdapter.install()` has run, for the reason
`pythonx/compose/ui/modifier.py`'s module docstring already gives for `pythonx.compose.ui.modifier`:
`register_package('pythonx.compose', 'androidx.compose')` makes `pythonx.compose` a synthetic package
with `__path__ = []`, and Python's import machinery passes that empty path to *every* finder for
*every* submodule underneath it -- so no on-disk file under `pythonx/compose/` is importable by its
own dotted name, regardless of whether the specific submodule (`runtime`, `material3`, `ui.modifier`,
...) itself corresponds to anything walked. `tests/test_runtime_module.py`'s
`TheModuleIsUnreachableByOrdinaryImport` checks this directly against the real adapter source
(`tests/adapter.py` reads `PythonxAdapter.SOURCE` unmodified) rather than assuming it by analogy:
`import pythonx.compose.runtime` raises `ModuleNotFoundError` once the layer is installed, the same
as `import pythonx.compose.material3` does for a name the walked table never produced.

`modifier.py` works around this by being loaded out of band
(`importlib.util.spec_from_file_location`, never as `pythonx.compose.ui.modifier`), and this file
needs the same treatment. Closing the gap for real -- a packaging route, or an adapter-side seam that
does not collide with `register_package` -- is `docs/pythonx-adapter-design.md` §2.5's open item in
`PythonMultiplatform`, and is not something editing this file can do. Until it closes, an application
loads this module the way `tests/test_runtime_module.py` and `tests/test_modifier_module.py` do: by
path, under whatever name it chooses, and reads [Composable] off the result.
"""

from __future__ import annotations


def Composable(target):
    """Identity. `UI.ipynb` writes `@Composable def Screen(): ...`; nothing needs to happen to
    `Screen` for that to work, because the composer every nested `pythonx.compose.*` call needs is
    threaded by `PythonComposition`/`pythonx._bind_composable` from the *callee's* declared slot
    type, not from anything the caller -- decorated or not -- does. See the module docstring for
    what used to be here and why it is gone.
    """
    return target
