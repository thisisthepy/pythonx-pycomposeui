from pythonx.compose.runtime import Composable

from androidx.compose.material3 import CardKt

__COMPILED_CODE__ = None
Unit = None

class Card(Composable):
    """ M3 filled card """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = CardKt.Card
            except Exception:
                for name, obj in CardKt.__dict__.items():
                    if name.startswith("Card-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("Card is cannot be found")

    def compose(
            self,
            modifier=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            elevation=__COMPILED_CODE__,
            border=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            modifier=modifier,
            shape=shape,
            colors=colors,
            elevation=elevation,
            border=border,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )


class ElevatedCard(Composable):
    """ M3 elevated card """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = CardKt.ElevatedCard
            except Exception:
                for name, obj in CardKt.__dict__.items():
                    if name.startswith("ElevatedCard-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("ElevatedCard is cannot be found")

    def compose(
            self,
            modifier=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            elevation=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            modifier=modifier,
            shape=shape,
            colors=colors,
            elevation=elevation,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )


class OutlinedCard(Composable):
    """ M3 outlined card """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = CardKt.OutlinedCard
            except Exception:
                for name, obj in CardKt.__dict__.items():
                    if name.startswith("OutlinedCard-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("OutlinedCard is cannot be found")

    def compose(
            self,
            modifier=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            elevation=__COMPILED_CODE__,
            border=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            modifier=modifier,
            shape=shape,
            colors=colors,
            elevation=elevation,
            border=border,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )