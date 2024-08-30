from pythonx.compose.runtime import Composable

from androidx.compose.material3 import BadgeKt

@Composable
class Badge(Composable):
    """ M3 badge """

    @classmethod
    def compose(
            cls,
            modifier,
            container_color,
            content_color,
            content
    ):
        getattr(BadgeKt, "Badge-eopBjH0")(
            modifier=modifier,
            containerColor=container_color,
            contentColor=content_color,
            content=content,
            c=cls.composer,
            changed=1
        )


@Composable
class BadgedBox(Composable):
    """ M3 badged box """

    @classmethod
    def compose(
            cls,
            badge,
            modifier,
            content
    ):
        BadgeKt.BadgedBox(
            badge=badge,
            modifier=modifier,
            content=content,
            c=cls.composer,
            changed=1
        )