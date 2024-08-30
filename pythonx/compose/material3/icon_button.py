from pythonx.compose.runtime import Composable

from androidx.compose.material3 import IconButtonKt

__COMPILED_CODE__ = None
Unit = None

class IconButton(Composable):
    """ M3 standard icon button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconButtonKt.IconButton
            except Exception:
                for name, obj in IconButtonKt.__dict__.items():
                    if name.startswith("IconButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("IconButton is cannot be found")

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


class FilledIconButton(Composable):
    """ M3 filled icon button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconButtonKt.FilledIconButton
            except Exception:
                for name, obj in IconButtonKt.__dict__.items():
                    if name.startswith("FilledIconButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("FilledIconButton is cannot be found")

    def compose(
            self,
            on_click,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
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
            onClick=on_click,
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


class FilledTonalIconButton(Composable):
    """ M3 filled tonal icon button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconButtonKt.FilledTonalIconButton
            except Exception:
                for name, obj in IconButtonKt.__dict__.items():
                    if name.startswith("FilledTonalIconButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("FilledTonalIconButton is cannot be found")

    def compose(
            self,
            on_click,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
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
            onClick=on_click,
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


class OutlinedIconButton(Composable):
    """ M3 outlined icon button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconButtonKt.OutlinedIconButton
            except Exception:
                for name, obj in IconButtonKt.__dict__.items():
                    if name.startswith("OutlinedIconButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("OutlinedIconButton is cannot be found")

    def compose(
            self,
            on_click,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            border=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
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