from __future__ import annotations

class Alignment:
    """
    An interface to calculate the position of a sized box inside an available space.
    Alignment is often used to define the alignment of a layout inside a parent layout.

    NOTE: Alignment and its constants (like `Alignment.Center`) are currently blocked
    upstream. The `ArtifactScanner` only binds top-level functions and value-class
    constructors; it does not generate bindings or object handles for static properties
    or interface companion objects.
    The previous chaquopy (`jclass`) code was removed because it dies at import time
    (`ModuleNotFoundError: No module named 'java'`).
    """
    pass

class AbsoluteAlignment:
    """
    A collection of common Alignments unaware of the layout direction.

    NOTE: Unbound for the same reason as `Alignment` — `ArtifactScanner` does not
    produce object handles for these constants.
    """
    pass
