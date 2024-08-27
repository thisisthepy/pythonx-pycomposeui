# pythonx - pycomposeui

> pythonx is a python extension for kotlin integration

### Description

Python Wrapper for Kotlin Compose Multiplatform.


#### Maintainer
| Name       | Detailed Part       | Period     |
|------------|---------------------|------------|
| @b-re-w    | Composable Runtime  | 2023 ~ now |
| @rnoro5122 | Material3           | 2024 ~ now |



### Template ToDo list
- [x] Composable Runtime
- [x] Material3 Wrapper


___

## Integration

---

## Usage
```python
from pycomposeui.runtime import Composable, EmptyComposable, remember_saveable
from pycomposeui.material3 import Text, Column, Row, Button
from pycomposeui.ui import modifier, Alignment


@Composable
def UiTestCase(text: str = "UiTestCase"):
    """ Simple way to create a Composable """
    Text(text)


@Composable
class UiTest:
    """ Class-based Composable """
    def compose(self, content: Composable = EmptyComposable):
        Column(modifier, content=lambda: {
            UiTestCase(text="UiTestCase in UiTest"),
            content()
        })


@Composable
class BasicText:
    """ Class-based Composable 2 """
    @classmethod
    def compose(cls, text: str = "BasicText"):
        Text(text)


@Composable
class RichText(Composable):
    """ Inheritance-based Composable """
    @staticmethod
    def compose(content: Composable = EmptyComposable):
        Column(modifier, content=Composable(lambda: {
            Text("Basic Text inside of Rich Text"),
            Row(lambda: {  # Unlike Kotlin Compose, pycompose does not require Composable functions as content parameters
                Text("Row Left Side  "),
                Text("Row Right Side")
            }),
            content()
        }))

```
