# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

def do_quest():
    touch(Template(r"tpl1611060685104.png", record_pos=(-0.454, 0.125), resolution=(2560, 1440)))
    sleep(1)
    touch(Template(r"tpl1618392386784.png", record_pos=(-0.432, 0.198), resolution=(2560, 1440)))

    sleep(0.5)
    touch(Template(r"tpl1611060782301.png", record_pos=(0.001, -0.113), resolution=(2560, 1440)))

    chests = [p([0.389, 0.205]), p([0.503, 0.209]), p([0.606, 0.199]), p([0.718, 0.197]), p([0.826, 0.205])]
    for chest in chests:
        sleep(1)
        touch(chest)
        sleep(1.5)
        touch(p([0.806, 0.233]))
    sleep(1)
    touch(Template(r"tpl1611061136772.png", record_pos=(0.46, -0.255), resolution=(2560, 1440)))
    sleep(1)
    return