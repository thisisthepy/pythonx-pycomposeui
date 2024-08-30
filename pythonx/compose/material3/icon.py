from pythonx.compose.runtime import Composable

from androidx.compose.material3 import IconKt

__COMPILED_CODE__ = None
Unit = None

class Icon(Composable):
    """ M3 icon """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = IconKt.Icon
            except Exception:
                for name, obj in IconKt.__dict__.items():
                    if name.startswith("Icon-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("Icon is cannot be found")

    def compose(
            self,
            bitmap=__COMPILED_CODE__,
            content_description=__COMPILED_CODE__,
            modifier=__COMPILED_CODE__,
            tint=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            bitmap=bitmap,
            contentDescription=content_description,
            modifier=modifier,
            tint=tint,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )