# -*- coding: utf-8 -*-

import ctypes
from ctypes.util import find_library


libopus = ctypes.CDLL(find_library('opus'))


strerror = libopus.opus_strerror
strerror.argtypes = (ctypes.c_int,)
strerror.restype = ctypes.c_char_p
strerror.__doc__ = '''Converts an opus error code into a human readable string'''


get_version_string = libopus.opus_get_version_string
get_version_string.argtypes = None
get_version_string.restype = ctypes.c_char_p
get_version_string.__doc__ = 'Gets the libopus version string'


if __name__ == '__main__':
    print get_version_string()
    print strerror(-1)
    print strerror(-2)
    print strerror(-3)
    print strerror(-4)
    print strerror(-5)
