from pythonx.compose.runtime import Composable

from androidx.compose.material3 import TextFieldKt

__COMPILED_CODE__ = None
Unit = None

class TextField(Composable):
    """ M3 filled text field """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = TextFieldKt.TextField
            except Exception:
                for name, obj in TextFieldKt.__dict__.items():
                    if name.startswith("TextField-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("TextField is cannot be found")

    def compose(
            self,
            value=__COMPILED_CODE__,
            on_value_change=__COMPILED_CODE__,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            read_only=__COMPILED_CODE__,
            text_style=__COMPILED_CODE__,
            label=__COMPILED_CODE__,
            placeholder=__COMPILED_CODE__,
            leading_icon=__COMPILED_CODE__,
            trailing_icon=__COMPILED_CODE__,
            prefix=__COMPILED_CODE__,
            suffix=__COMPILED_CODE__,
            support_text=__COMPILED_CODE__,
            is_error=__COMPILED_CODE__,
            visual_transformation=__COMPILED_CODE__,
            keyboard_options=__COMPILED_CODE__,
            keyboard_actions=__COMPILED_CODE__,
            single_line=__COMPILED_CODE__,
            max_lines=__COMPILED_CODE__,
            min_lines=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            value=value,
            onValueChange=on_value_change,
            modifier=modifier,
            enabled=enabled,
            readOnly=read_only,
            textStyle=text_style,
            label=label,
            placeholder=placeholder,
            leadingIcon=leading_icon,
            trailingIcon=trailing_icon,
            prefix=prefix,
            suffix=suffix,
            supportingText=support_text,
            isError=is_error,
            visualTransformation=visual_transformation,
            keyboardOptions=keyboard_options,
            keyboardActions=keyboard_actions,
            singleLine=single_line,
            maxLines=max_lines,
            minLines=min_lines,
            interactionSource=interaction_source,
            shape=shape,
            colors=colors,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )


class OutlinedTextField(Composable):
    """ M3 outlined text field """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = TextFieldKt.OutlinedTextField
            except Exception:
                for name, obj in TextFieldKt.__dict__.items():
                    if name.startswith("OutlinedTextField-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("OutlinedTextField is cannot be found")

    def compose(
            self,
            value=__COMPILED_CODE__,
            on_value_change=__COMPILED_CODE__,
            modifier=__COMPILED_CODE__,
            enabled=__COMPILED_CODE__,
            read_only=__COMPILED_CODE__,
            text_style=__COMPILED_CODE__,
            label=__COMPILED_CODE__,
            placeholder=__COMPILED_CODE__,
            leading_icon=__COMPILED_CODE__,
            trailing_icon=__COMPILED_CODE__,
            prefix=__COMPILED_CODE__,
            suffix=__COMPILED_CODE__,
            support_text=__COMPILED_CODE__,
            is_error=__COMPILED_CODE__,
            visual_transformation=__COMPILED_CODE__,
            keyboard_options=__COMPILED_CODE__,
            keyboard_actions=__COMPILED_CODE__,
            single_line=__COMPILED_CODE__,
            max_lines=__COMPILED_CODE__,
            min_lines=__COMPILED_CODE__,
            interaction_source=__COMPILED_CODE__,
            shape=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            value=value,
            onValueChange=on_value_change,
            modifier=modifier,
            enabled=enabled,
            readOnly=read_only,
            textStyle=text_style,
            label=label,
            placeholder=placeholder,
            leadingIcon=leading_icon,
            trailingIcon=trailing_icon,
            prefix=prefix,
            suffix=suffix,
            supportingText=support_text,
            isError=is_error,
            visualTransformation=visual_transformation,
            keyboardOptions=keyboard_options,
            keyboardActions=keyboard_actions,
            singleLine=single_line,
            maxLines=max_lines,
            minLines=min_lines,
            interactionSource=interaction_source,
            shape=shape,
            colors=colors,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )