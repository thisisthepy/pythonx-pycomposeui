from runtime import Composable
from thisisthepy.pycomposeui import Material3Kt

_Text = Material3Kt.SimpleTextWidget
_Spacer = Material3Kt.SimpleSpacer
_Card = Material3Kt.SimpleCardWidget
_Button = Material3Kt.SimpleButtonWidget


@Composable
def Text(text: str, color: int = 0xff000000, font_size: float = 12.0, composer=None):
    return _Text(text, color, font_size, composer, 1)


@Composable
def Spacer(start: float = 0.0, top: float = 0.0, end: float = 0.0, bottom: float = 0.0, composer=None):
    return _Spacer(start, top, end, bottom, composer, 1)


@Composable
def Card(
        corner_radius: float = 10.0, color: int = 0xff745faa,
        composer=None, content: callable = lambda: None
):
    return _Card(corner_radius, color, content, composer, 1)


@Composable
def Button(
        on_click: callable, enabled: bool = True, corner_radius: float = 10.0,
        color: int = 0xff745faa, composer=None, content: callable = lambda: None
):
    return _Button(on_click, enabled, corner_radius, color, content, composer, 1)
