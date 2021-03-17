# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *

def init_resolution():
    global x
    global y
    y = G.DEVICE.display_info['height']
    x = G.DEVICE.display_info['width']
    return

def p(point):
    return [point[0] * x, point[1] * y]
