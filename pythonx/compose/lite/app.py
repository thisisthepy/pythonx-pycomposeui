import jvm

jvm.init_jvm()  # Initialize the JVM

from org.example.project import AppKt

from material3 import Text, Spacer, Card, Button
from runtime import Composable, register_composer


@Composable
def MainScreen(*args, **kwargs):
    """ Main Screen Composable """
    Text("Welcome to Compose for Desktop with Python!", font_size=20.0)
    Spacer(start=0, top=10.0, end=0, bottom=10.0)
    Button(
        on_click=lambda: print("Card Clicked"),
        color=0xfff14f4d,
        content=lambda: Text("This is a Card Composable", color=0xffffffff),
    )


AppKt.launch(MainScreen, register_composer)  # Launch the App
