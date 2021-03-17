# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
from random import choice
using("common.air")
from common import *


def do_ares(times=10):
    for i in range(times):
        play_one_game()
        if exists(Template(r"tpl1615914034297.png", threshold=0.9, record_pos=(0.316, 0.125), resolution=(2560, 1440))):
            break
    return


skills = [[0.041, 0.725], [0.128, 0.795], [0.162, 0.927]]

cards = [[0.339, 0.853], [0.451, 0.838], [0.55, 0.84], [0.662, 0.84]]

pos = [[0.198, 0.34], [0.301, 0.349], [0.4, 0.353],
       [0.287, 0.481], [0.399, 0.478], 
       [0.148, 0.626], [0.251, 0.635], [0.391, 0.603]]

def play_one_match():
    touch(p([0.287, 0.626]))
    try:
        touch(Template(r"tpl1615912009557.png", record_pos=(0.317, 0.125), resolution=(2560, 1440)))
        sleep(10)
        wait(Template(r"tpl1615912039486.png", record_pos=(-0.391, 0.179), resolution=(2560, 1440)), timeout=20)
    except:
        return False

    for i in range(1000):
        sleep(0.5)
        touch(p(choice(skills)))
        sleep(0.5)
        touch(p(choice(cards)))
        sleep(0.5)
        touch(p(choice(pos)))
        sleep(0.5)
        touch(p(choice(pos)))
        if i % 10 == 0:
            if exists(Template(r"tpl1615912009557.png", record_pos=(0.317, 0.125), resolution=(2560, 1440))):
                break
    return True

