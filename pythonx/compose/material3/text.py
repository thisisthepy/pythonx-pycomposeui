from pythonx.compose.runtime import Composable

from androidx.compose.material3 import TextKt

__COMPILED_CODE__ = None
Unit = None

class Text(Composable):
    """ M3 text """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = TextKt.Text
            except Exception:
                for name, obj in TextKt.__dict__.items():
                    if name.startswith("Text-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("Text is cannot be found")

    def compose(
            self,
            text=__COMPILED_CODE__,
            modifier=__COMPILED_CODE__,
            color=__COMPILED_CODE__,
            font_size=__COMPILED_CODE__,
            font_style=__COMPILED_CODE__,
            font_weight=__COMPILED_CODE__,
            font_family=__COMPILED_CODE__,
            letter_spacing=__COMPILED_CODE__,
            text_decoration=__COMPILED_CODE__,
            text_align=__COMPILED_CODE__,
            line_height=__COMPILED_CODE__,
            overflow=__COMPILED_CODE__,
            soft_wrap=__COMPILED_CODE__,
            max_lines=__COMPILED_CODE__,
            min_lines=__COMPILED_CODE__,
            on_text_layout=__COMPILED_CODE__,
            style=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            text=text,
            modifier=modifier,
            color=color,
            fontSize=font_size,
            fontStyle=font_style,
            fontWeight=font_weight,
            fontFamily=font_family,
            letterSpacing=letter_spacing,
            textDecoration=text_decoration,
            textAlign=text_align,
            lineHeight=line_height,
            overflow=overflow,
            softWrap=soft_wrap,
            maxLines=max_lines,
            minLines=min_lines,
            onTextLayout=on_text_layout,
            style=style,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )