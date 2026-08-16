from androidx.compose.material3 import IconKt

__COMPILED_CODE__ = None
Unit = None

class Icon:
    """ M3 icon.

    Not usable -- kept only because `PythonMultiplatform` commit `a6742a1c` pinned `Icon` as
    unreachable through the walked adaptation table (every overload needs an `ImageBitmap`,
    `ImageVector` or `Painter`, and nothing walked produces one), so this hand-written wrapper is the
    only Python-facing record of that. It does not subclass `pythonx.compose.runtime.Composable`
    (`7d6c0a1` made that name a plain identity-decorator function, not a base class -- inheriting from
    it raises `TypeError` at class-definition time, which used to break importing this whole package,
    not just this declaration). `compose()` below still reaches for `self.composer`, which nothing
    sets; calling it fails, which is correct, since the declaration cannot be reached this way either.
    """

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