# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

def do_expedition(starts_from_menu=True, times=100):
    if starts_from_menu:
        touch(Template(r"tpl1610545944717.png", record_pos=(0.148, -0.002), resolution=(2560, 1440)))
        sleep(2)
        swipe(Template(r"tpl1610545963802.png", record_pos=(0.354, -0.012), resolution=(2560, 1440)), vector=[-0.5772, -0.0113])
        sleep(2)
        touch(Template(r"tpl1610545996989.png", record_pos=(0.109, 0.063), resolution=(2560, 1440)))
        # TODO: add raid
        sleep(1)
    repeat(times)
    if starts_from_menu:
        sleep(1)
        touch(Template(r"tpl1610546035602.png", record_pos=(0.46, -0.252), resolution=(2560, 1440)))
        sleep(2)
        touch(Template(r"tpl1610546035602.png", record_pos=(0.46, -0.252), resolution=(2560, 1440)))
        sleep(1)
    return


def repeat(times=100):
    pos = [
        p([0.884, 0.602]),
        p([0.671, 0.605]),
        p([0.486, 0.592]),
        p([0.283, 0.589]),
        p([0.096, 0.572]),
    ]
    for i in range(times):
        challenge = exists(Template(r"tpl1610008918490.png", record_pos=(-0.405, 0.018), resolution=(2560, 1440)))
        if challenge:
            touch(challenge)
        else:
            for tpl in pos:
                touch(tpl)
        sleep(3)
        touch(Template(r"tpl1610009118872.png", record_pos=(0.421, 0.185), resolution=(2560, 1440)))
        sleep(5)
        for i in range(3):
            manual = exists(Template(r"tpl1610450811926.png", record_pos=(0.459, -0.012), resolution=(2560, 1440)))
            if manual:
                touch(manual)
                break
        sleep(60)
        for i in range(30):
            victory = exists(Template(r"tpl1610009240936.png", record_pos=(0.165, -0.178), resolution=(2560, 1440)))
            if victory:
                sleep(3)
                touch(victory)
                break
            failure = exists(Template(r"tpl1610009455255.png", record_pos=(0.219, -0.197), resolution=(2560, 1440)))
            if failure:
                sleep(3)
                touch(failure)
                break
        sleep(3)
        accepted = exists(Template(r"tpl1610010355044.png", record_pos=(-0.004, 0.117), resolution=(2560, 1440)))
        if accepted:
            touch(accepted)
            sleep(3)
    return
