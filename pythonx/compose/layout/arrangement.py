from __future__ import annotations

class Arrangement:
    """
    Used to specify the horizontal arrangement of the layout's children in layouts like [Row].

    NOTE: Arrangement and its constants (like `Arrangement.SpaceBetween`) are currently
    blocked upstream. The `ArtifactScanner` only binds top-level functions and value-class
    constructors; it does not generate bindings or object handles for static properties
    or objects.
    The previous chaquopy (`jclass`) code was removed because it dies at import time
    (`ModuleNotFoundError: No module named 'java'`).
    """
    pass
