from __future__ import annotations

"""`pythonx/compose/ui/alignment.py` -- what the adaptation layer now produces, and how to spell it.

`Alignment` and its constants used to be blocked: the walker bound top-level functions and, later,
value-class constructors, and a constant held by a companion was neither. `PythonMultiplatform`'s
`80318c16` added that binding (`CallableKind.STATIC_GETTER`), and `6d896fba` proved a constant
crosses and changes a layout.

So there is nothing to wrap here, and that is the point: this package's rule is that whatever the
adaptation layer produces gets no hand-written wrapper (`0856d08`, `f7e21f8`). What this file is for
is the two things a caller cannot read off the layer.

## The names the layer produces

    Bottom  BottomCenter  BottomEnd  BottomStart  Center  CenterEnd  CenterHorizontally
    CenterStart  CenterVertically  End  Start  Top  TopCenter  TopEnd  TopStart

Read out of the walked table, not from Compose's own source: a name Compose declares but the walker
declines would not be here.

## They are called, not read

    from pythonx.compose.ui import Alignment
    Alignment.Center()          # with the parentheses

The layer renders every declaration as a callable and does not branch on the kind column, so a
static getter arrives as a zero-argument function rather than an attribute. Writing `Alignment.Center`
passes the function object itself, and the dispatcher refuses it -- upstream `6d896fba` records the
message ("expected a Horizontal handle", for the arrangement case). Exposing these as attributes is
upstream's next step; the column that would drive it already exists.
"""
