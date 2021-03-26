# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

def do_guild(gem=5, gold=0):
    touch(Template(r"tpl1616595040011.png", record_pos=(0.301, 0.158), resolution=(2560, 1440)))
    sleep(1)
    touch(Template(r"tpl1616595071524.png", record_pos=(-0.163, 0.043), resolution=(2560, 1440)))
    wait(Template(r"tpl1616595112577.png", record_pos=(0.402, 0.1), resolution=(2560, 1440)))
    sleep(0.5)
    touch(p([0.904, 0.674]))
    sleep(1)
    for _ in range(gem):
        touch(Template(r"tpl1616595183750.png", record_pos=(0.095, 0.155), resolution=(2560, 1440)))
        sleep(0.5)
    for _ in range(gold):
        touch(Template(r"tpl1616685979950.png", record_pos=(-0.166, 0.156), resolution=(1920, 1080)))
        sleep(0.5)
    for _ in range(3):
        touch(Template(r"tpl1616595251634.png", record_pos=(0.314, -0.211), resolution=(2560, 1440)))
        sleep(0.5)
    return

