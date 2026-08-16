"""M3 icon toggle buttons -- the half of this file that is still hand-written, and why the other
half is not.

`IconButton`, `FilledIconButton`, `FilledTonalIconButton` and `OutlinedIconButton` used to be here.
They are gone: `IconButton` is a walked declaration proven end to end
(`iconButtonComposesItsClickHandlerAndItsContent`, `PythonMultiplatform` commit `a6742a1c`,
`ComposableRenderTest.kt`) -- `from pythonx.compose.material3 import IconButton; IconButton(on_click=
lambda: None, content=lambda: Text('hi'))` renders real pixels with no wrapper at all -- and the
other three were the identical `__COMPILED_CODE__` / `find_composable` / `name.startswith("<Name>-")`
template with only the `*Kt` attribute changed, the same class of finding `buttons.py`'s deletion
documents for `Button`'s siblings.

The four classes below are not proven the same way and stay, but the reason is narrower than "the
slot type is unbound." Each takes `on_checked_change`, a `(Boolean) -> Unit` function-typed
parameter. That *is* bound in the walked table -- `ComposableBindingTest.kt:392` in
`PythonMultiplatform` asserts `Checkbox.onCheckedChange` resolves to exactly
`kotlin.Function1(kotlin.Boolean)->kotlin.Unit`, and it predates `728809bc`: composable-declaration
slots have gone through `functionSlotTypeName`, which already handled arbitrary `FunctionN` arity and
argument types, since the earlier commit `a179b747`. `728809bc` opened a *different* path
(non-`@Composable` plain function parameters, e.g. `Modifier.clickable`'s zero-argument `onClick`)
and does not bear on this one either way. So the type-level claim in the previous version of this
docstring was imprecise: `on_checked_change` is not declined.

What is missing is the render proof, and `ComposableRenderTest.kt` (same repository) says why one
does not exist yet, explicitly: a static render delivers no events, so a callback-shaped slot like
`onCheckedChange` "cannot be shown to work by rasterising anything" -- the ink-comparison proof
`IconButton`'s `on_click` got does not apply to a value that only changes on a click nothing in a
render call ever sends. No test anywhere renders `IconToggleButton`, `Checkbox`, `Switch`, `TextField`
or `OutlinedTextField` from Python, nor drives their callback and observes the result -- `Text.
onTextLayout` is the only callback-shaped slot with that proof, and it differs in kind (populated by
layout, not by a user event). `text_field.py`'s `on_value_change` -- `(String) -> Unit` -- is bound
the same way and is missing the same shape of proof. Until a render test exists for one of these
(some shape other than empty-vs-populated ink, since checked/unchecked and typed/untyped visuals may
not differ the way empty/populated content does), they stay hand-written rather than removed.
"""

from pythonx.compose.runtime import Composable

from androidx.compose.material3 import IconButtonKt

__COMPILED_CODE__ = None
Unit = None


class IconToggleButton(Composable):
    """ M3 standard icon toggle button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconButtonKt.IconToggleButton
            except Exception:
                for name, obj in IconButtonKt.__dict__.items():
                    if name.startswith("IconToggleButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("IconToggleButton is cannot be found")

    def compose(
            self,
            checked=__COMPILED_CODE__,
            on_checked_change=__COMPILED_CODE__,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            checked=checked,
            onCheckedChange=on_checked_change,
            modifier=modifier,
            enabled=enabled,
            colors=colors,
            interactionSource=interaction_source,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )


class FilledIconToggleButton(Composable):
    """ M3 filled icon toggle button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconButtonKt.FilledIconToggleButton
            except Exception:
                for name, obj in IconButtonKt.__dict__.items():
                    if name.startswith("FilledIconToggleButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("FilledIconToggleButton is cannot be found")

    def compose(
            self,
            checked=__COMPILED_CODE__,
            on_checked_change=__COMPILED_CODE__,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            checked=checked,
            onCheckedChange=on_checked_change,
            modifier=modifier,
            enabled=enabled,
            shape=shape,
            colors=colors,
            interactionSource=interaction_source,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )


class FilledTonalIconToggleButton(Composable):
    """ M3 filled tonal icon toggle button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconButtonKt.FilledTonalIconToggleButton
            except Exception:
                for name, obj in IconButtonKt.__dict__.items():
                    if name.startswith("FilledTonalIconToggleButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("FilledTonalIconToggleButton is cannot be found")

    def compose(
            self,
            on_click,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            elevation=__COMPILED_CODE__,
            border=__COMPILED_CODE__,
            content_padding=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            modifier=modifier,
            enabled=enabled,
            shape=shape,
            colors=colors,
            elevation=elevation,
            border=border,
            contentPadding=content_padding,
            interactionSource=interaction_source,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            onClick=on_click,
            **kwargs,
            c=self.composer,
            changed=1
        )


class OutlinedIconToggleButton(Composable):
    """ M3 outlined icon toggle button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconButtonKt.OutlinedIconToggleButton
            except Exception:
                for name, obj in IconButtonKt.__dict__.items():
                    if name.startswith("OutlinedIconToggleButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("OutlinedIconToggleButton is cannot be found")

    def compose(
            self,
            checked=__COMPILED_CODE__,
            on_checked_change=__COMPILED_CODE__,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            border=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            checked=checked,
            onCheckedChange=on_checked_change,
            modifier=modifier,
            enabled=enabled,
            shape=shape,
            colors=colors,
            border=border,
            interactionSource=interaction_source,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )
