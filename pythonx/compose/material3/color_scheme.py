from androidx.compose.material3 import ColorSchemeKt
from androidx.compose.material3 import ColorScheme

__COMPILED_CODE__ = None
Unit = None

class ColorScheme:
    """ M3 color scheme.

    Not usable -- kept only because `PythonMultiplatform` commit `a6742a1c` pinned `ColorScheme`'s
    factories as unreachable through the walked adaptation table (36 `Color` parameters, all
    defaulted in Kotlin, none omittable in the binding, against a 6-parameter omission cap), so this
    hand-written wrapper is the only Python-facing record of that. It does not subclass
    `pythonx.compose.runtime.Composable` (`7d6c0a1` made that name a plain identity-decorator
    function, not a base class -- inheriting from it raises `TypeError` at class-definition time,
    which used to break importing this whole package, not just this declaration). `compose()` below
    still reaches for `self.composer`, which nothing sets; calling it fails, which is correct, since
    the declaration cannot be reached this way either.
    """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ColorScheme
            except Exception:
                for name, obj in ColorSchemeKt.__dict__.items():
                    if name.startswith("ColorScheme-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("ColorScheme is cannot be found")

    def compose(
            self,
            primary=__COMPILED_CODE__,
            on_primary=__COMPILED_CODE__,
            primary_container=__COMPILED_CODE__,
            on_primary_container=__COMPILED_CODE__,
            inverse_primary=__COMPILED_CODE__,
            secondary=__COMPILED_CODE__,
            on_secondary=__COMPILED_CODE__,
            secondary_container=__COMPILED_CODE__,
            on_secondary_container=__COMPILED_CODE__,
            tertiary=__COMPILED_CODE__,
            on_tertiary=__COMPILED_CODE__,
            tertiary_container=__COMPILED_CODE__,
            on_tertiary_container=__COMPILED_CODE__,
            background=__COMPILED_CODE__,
            on_background=__COMPILED_CODE__,
            surface=__COMPILED_CODE__,
            on_surface=__COMPILED_CODE__,
            surface_variant=__COMPILED_CODE__,
            on_surface_variant=__COMPILED_CODE__,
            surface_tint=__COMPILED_CODE__,
            inverse_surface=__COMPILED_CODE__,
            inverse_on_surface=__COMPILED_CODE__,
            error=__COMPILED_CODE__,
            on_error=__COMPILED_CODE__,
            error_container=__COMPILED_CODE__,
            on_error_container=__COMPILED_CODE__,
            outline=__COMPILED_CODE__,
            outline_variant=__COMPILED_CODE__,
            scrim=__COMPILED_CODE__,
            surface_bright=__COMPILED_CODE__,
            surface_dim=__COMPILED_CODE__,
            surface_container=__COMPILED_CODE__,
            surface_container_high=__COMPILED_CODE__,
            surface_container_highest=__COMPILED_CODE__,
            surface_container_low=__COMPILED_CODE__,
            surface_container_lowest=__COMPILED_CODE__,
    ):
        kwargs = { key: value for key, value in dict(
            primary=primary,
            onPrimary=on_primary,
            primaryContainer=primary_container,
            onPrimaryContainer=on_primary_container,
            inversePrimary=inverse_primary,
            secondary=secondary,
            onSecondary=on_secondary,
            secondaryContainer=secondary_container,
            onSecondaryContainer=on_secondary_container,
            tertiary=tertiary,
            onTertiary=on_tertiary,
            tertiaryContainer=tertiary_container,
            onTertiaryContainer=on_tertiary_container,
            background=background,
            onBackground=on_background,
            surface=surface,
            onSurface=on_surface,
            surfaceVariant=surface_variant,
            onSurfaceVariant=on_surface_variant,
            surfaceTint=surface_tint,
            inverseSurface=inverse_surface,
            inverseOnSurface=inverse_on_surface,
            error=error,
            onError=on_error,
            errorContainer=error_container,
            onErrorContainer=on_error_container,
            outline=outline,
            outlineVariant=outline_variant,
            scrim=scrim,
            surfaceBright=surface_bright,
            surfaceDim=surface_dim,
            surfaceContainer=surface_container,
            surfaceContainerHigh=surface_container_high,
            surfaceContainerHighest=surface_container_highest,
            surfaceContainerLow=surface_container_low,
            surfaceContainerLowest=surface_container_lowest


        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )


class lightColorScheme:
    """ M3 light color scheme.

    Not usable -- see `ColorScheme`'s docstring above: `a6742a1c` pinned this factory unreachable
    (36 `Color` parameters against a 6-parameter omission cap), and this no longer subclasses
    `pythonx.compose.runtime.Composable` for the same class-definition-time `TypeError` reason.
    """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ColorSchemeKt.lightColorScheme
            except Exception:
                for name, obj in ColorSchemeKt.__dict__.items():
                    if name.startswith("lightColorScheme-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("lightColorScheme is cannot be found")

    def compose(
            self,
            primary=__COMPILED_CODE__,
            on_primary=__COMPILED_CODE__,
            primary_container=__COMPILED_CODE__,
            on_primary_container=__COMPILED_CODE__,
            inverse_primary=__COMPILED_CODE__,
            secondary=__COMPILED_CODE__,
            on_secondary=__COMPILED_CODE__,
            secondary_container=__COMPILED_CODE__,
            on_secondary_container=__COMPILED_CODE__,
            tertiary=__COMPILED_CODE__,
            on_tertiary=__COMPILED_CODE__,
            tertiary_container=__COMPILED_CODE__,
            on_tertiary_container=__COMPILED_CODE__,
            background=__COMPILED_CODE__,
            on_background=__COMPILED_CODE__,
            surface=__COMPILED_CODE__,
            on_surface=__COMPILED_CODE__,
            surface_variant=__COMPILED_CODE__,
            on_surface_variant=__COMPILED_CODE__,
            surface_tint=__COMPILED_CODE__,
            inverse_surface=__COMPILED_CODE__,
            inverse_on_surface=__COMPILED_CODE__,
            error=__COMPILED_CODE__,
            on_error=__COMPILED_CODE__,
            error_container=__COMPILED_CODE__,
            on_error_container=__COMPILED_CODE__,
            outline=__COMPILED_CODE__,
            outline_variant=__COMPILED_CODE__,
            scrim=__COMPILED_CODE__,
            surface_bright=__COMPILED_CODE__,
            surface_dim=__COMPILED_CODE__,
            surface_container=__COMPILED_CODE__,
            surface_container_high=__COMPILED_CODE__,
            surface_container_highest=__COMPILED_CODE__,
            surface_container_low=__COMPILED_CODE__,
            surface_container_lowest=__COMPILED_CODE__,
    ):
        kwargs = { key: value for key, value in dict(
            primary=primary,
            onPrimary=on_primary,
            primaryContainer=primary_container,
            onPrimaryContainer=on_primary_container,
            inversePrimary=inverse_primary,
            secondary=secondary,
            onSecondary=on_secondary,
            secondaryContainer=secondary_container,
            onSecondaryContainer=on_secondary_container,
            tertiary=tertiary,
            onTertiary=on_tertiary,
            tertiaryContainer=tertiary_container,
            onTertiaryContainer=on_tertiary_container,
            background=background,
            onBackground=on_background,
            surface=surface,
            onSurface=on_surface,
            surfaceVariant=surface_variant,
            onSurfaceVariant=on_surface_variant,
            surfaceTint=surface_tint,
            inverseSurface=inverse_surface,
            inverseOnSurface=inverse_on_surface,
            error=error,
            onError=on_error,
            errorContainer=error_container,
            onErrorContainer=on_error_container,
            outline=outline,
            outlineVariant=outline_variant,
            scrim=scrim,
            surfaceBright=surface_bright,
            surfaceDim=surface_dim,
            surfaceContainer=surface_container,
            surfaceContainerHigh=surface_container_high,
            surfaceContainerHighest=surface_container_highest,
            surfaceContainerLow=surface_container_low,
            surfaceContainerLowest=surface_container_lowest


        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )


class darkColorScheme:
    """ M3 dark color scheme.

    Not usable -- see `ColorScheme`'s docstring above: `a6742a1c` pinned this factory unreachable
    (36 `Color` parameters against a 6-parameter omission cap), and this no longer subclasses
    `pythonx.compose.runtime.Composable` for the same class-definition-time `TypeError` reason.
    """

    def __init__(self):
        super().__init__()
        self.__kotlin_composable = None

    def find_composable(self):
        super().__init__()

        if self.__kotlin_composable is None:
            try:
                self.__kotlin_composable = ColorSchemeKt.darkColorScheme
            except Exception:
                for name, obj in ColorSchemeKt.__dict__.items():
                    if name.startswith("darkColorScheme-"):
                        self.__kotlin_composable = obj
                        break

        if not self.__kotlin_composable:
            raise Exception("darkColorScheme is cannot be found")

    def compose(
            self,
            primary=__COMPILED_CODE__,
            on_primary=__COMPILED_CODE__,
            primary_container=__COMPILED_CODE__,
            on_primary_container=__COMPILED_CODE__,
            inverse_primary=__COMPILED_CODE__,
            secondary=__COMPILED_CODE__,
            on_secondary=__COMPILED_CODE__,
            secondary_container=__COMPILED_CODE__,
            on_secondary_container=__COMPILED_CODE__,
            tertiary=__COMPILED_CODE__,
            on_tertiary=__COMPILED_CODE__,
            tertiary_container=__COMPILED_CODE__,
            on_tertiary_container=__COMPILED_CODE__,
            background=__COMPILED_CODE__,
            on_background=__COMPILED_CODE__,
            surface=__COMPILED_CODE__,
            on_surface=__COMPILED_CODE__,
            surface_variant=__COMPILED_CODE__,
            on_surface_variant=__COMPILED_CODE__,
            surface_tint=__COMPILED_CODE__,
            inverse_surface=__COMPILED_CODE__,
            inverse_on_surface=__COMPILED_CODE__,
            error=__COMPILED_CODE__,
            on_error=__COMPILED_CODE__,
            error_container=__COMPILED_CODE__,
            on_error_container=__COMPILED_CODE__,
            outline=__COMPILED_CODE__,
            outline_variant=__COMPILED_CODE__,
            scrim=__COMPILED_CODE__,
            surface_bright=__COMPILED_CODE__,
            surface_dim=__COMPILED_CODE__,
            surface_container=__COMPILED_CODE__,
            surface_container_high=__COMPILED_CODE__,
            surface_container_highest=__COMPILED_CODE__,
            surface_container_low=__COMPILED_CODE__,
            surface_container_lowest=__COMPILED_CODE__,
    ):
        kwargs = { key: value for key, value in dict(
            primary=primary,
            onPrimary=on_primary,
            primaryContainer=primary_container,
            onPrimaryContainer=on_primary_container,
            inversePrimary=inverse_primary,
            secondary=secondary,
            onSecondary=on_secondary,
            secondaryContainer=secondary_container,
            onSecondaryContainer=on_secondary_container,
            tertiary=tertiary,
            onTertiary=on_tertiary,
            tertiaryContainer=tertiary_container,
            onTertiaryContainer=on_tertiary_container,
            background=background,
            onBackground=on_background,
            surface=surface,
            onSurface=on_surface,
            surfaceVariant=surface_variant,
            onSurfaceVariant=on_surface_variant,
            surfaceTint=surface_tint,
            inverseSurface=inverse_surface,
            inverseOnSurface=inverse_on_surface,
            error=error,
            onError=on_error,
            errorContainer=error_container,
            onErrorContainer=on_error_container,
            outline=outline,
            outlineVariant=outline_variant,
            scrim=scrim,
            surfaceBright=surface_bright,
            surfaceDim=surface_dim,
            surfaceContainer=surface_container,
            surfaceContainerHigh=surface_container_high,
            surfaceContainerHighest=surface_container_highest,
            surfaceContainerLow=surface_container_low,
            surfaceContainerLowest=surface_container_lowest


        ) if value is not __COMPILED_CODE__ }

        if self.__kotlin_composable is None:
            self.find_composable()

        self.__kotlin_composable(
            **kwargs,
            c=self.composer,
            changed=1
        )