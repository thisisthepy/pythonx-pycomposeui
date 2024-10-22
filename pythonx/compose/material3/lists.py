from pythonx.compose.runtime import Composable

from androidx.compose.material3 import ListItemKt

__COMPILED_CODE__ = None
Unit = None

class ListItem(Composable):
    """ M3 list item """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ListItemKt.ListItem
            except Exception:
                for name, obj in ListItemKt.__dict__.items():
                    if name.startswith("ListItem-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("ListItem is cannot be found")

    def compose(
            self,
            headline_content=__COMPILED_CODE__,
            modifier=__COMPILED_CODE__,
            overline_content=__COMPILED_CODE__,
            supporting_content=__COMPILED_CODE__,
            leading_content=__COMPILED_CODE__,
            trailing_content=__COMPILED_CODE__,
            colors=__COMPILED_CODE__,
            tonal_elevation=__COMPILED_CODE__,
            shadow_elevation=__COMPILED_CODE__,
            content=__COMPILED_CODE__
    ):
        kwargs = { key: value for key, value in dict(
            headlineContent=headline_content,
            modifier=modifier,
            overlineContent=overline_content,
            supportingContent=supporting_content,
            leadingContent=leading_content,
            trailingContent=trailing_content,
            colors=colors,
            tonalElevation=tonal_elevation,
            shadowElevation=shadow_elevation,
            content=content
        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )