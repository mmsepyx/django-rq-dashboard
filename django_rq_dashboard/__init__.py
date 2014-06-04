VERSION = (0, 2, 2, "epyx")


def get_version():
    return ".".join(map(str, VERSION))

__version__ = get_version()
