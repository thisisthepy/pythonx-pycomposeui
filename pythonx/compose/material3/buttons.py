from pythonx.compose.runtime import Composable

from androidx.compose.material3 import ButtonKt

__COMPILED_CODE__ = None
Unit = None

class Button(Composable):
    """ M3 filled button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ButtonKt.Button
            except Exception:
                for name, obj in ButtonKt.__dict__.items():
                    if name.startswith("Button-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("Button is cannot be found")

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


class ElevatedButton(Composable):
    """ M3 elevated button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ButtonKt.ElevatedButton
            except Exception:
                for name, obj in ButtonKt.__dict__.items():
                    if name.startswith("ElevatedButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("ElevatedButton is cannot be found")

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


class FilledTonalButton(Composable):
    """ M3 filled tonal button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ButtonKt.FilledTonalButton
            except Exception:
                for name, obj in ButtonKt.__dict__.items():
                    if name.startswith("FilledTonalButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("FilledTonalButton is cannot be found")

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


class OutlinedButton(Composable):
    """ M3 outlined button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ButtonKt.OutlinedButton
            except Exception:
                for name, obj in ButtonKt.__dict__.items():
                    if name.startswith("OutlinedButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("OutlinedButton is cannot be found")

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


class TextButton(Composable):
    """ M3 text button """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ButtonKt.TextButton
            except Exception:
                for name, obj in ButtonKt.__dict__.items():
                    if name.startswith("TextButton-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("TextButton is cannot be found")

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
