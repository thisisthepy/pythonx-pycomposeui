from androidx.compose.material3 import ButtonKt


__COMPILED_CODE__ = None
Unit = None

class Modifier:
    __padding = None
    __fill_max_size = None


    def padding(self) -> "Modifier":
        def find_composable(self):
            super().__init__()

            if self.__padding is None:
                try:
                    self.__padding = ButtonKt.Button
                except Exception:
                    for name, obj in ButtonKt.__dict__.items():
                        if name.startswith("Button-"):
                            self.__padding = obj
                            break

            if not self.__padding:
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

        return self.__padding()

    def fill_max_size(self):
        return self