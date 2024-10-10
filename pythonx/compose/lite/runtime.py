_composer = None


def register_composer(composer):
    global _composer
    print("INFO: Registering composer...")
    _composer = composer


def Composable(func, *args, **kwargs):
    return lambda *args, **kwargs: func(*args, **kwargs, composer=_composer)
