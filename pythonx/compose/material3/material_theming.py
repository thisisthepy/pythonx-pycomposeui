from pythonx.compose.runtime import Composable

from androidx.compose.material3 import MaterialThemeKt

__COMPILED_CODE__ = None
Unit = None

class MaterialTheme(Composable):
    """ M3 theme """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = MaterialThemeKt.MaterialTheme
            except Exception:
                for name, obj in MaterialThemeKt.__dict__.items():
                    if name.startswith("MaterialTheme-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("MaterialTheme is cannot be found")

    def compose(
            self,
            color_scheme=__COMPILED_CODE__,
            shapes=__COMPILED_CODE__,
            typography=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            colorScheme=color_scheme,
            shapes=shapes,
            typography=typography,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )