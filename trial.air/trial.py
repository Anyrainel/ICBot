# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *

using("common.air")
from common import *

def do_trials(exp=10, gold=10, crystal=0):
    touch(Template(r"tpl1610617875824.png", record_pos=(0.147, 0.001), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610617897743.png", record_pos=(-0.347, 0.057), resolution=(2560, 1440)))
    sleep(1)
    touch(p([0.070, 0.186]))
    repeat_trial(exp)
    touch(Template(r"tpl1610618115769.png", record_pos=(-0.439, -0.096), resolution=(2560, 1440)))
    repeat_trial(gold)
    touch(Template(r"tpl1610618219303.png", record_pos=(-0.436, -0.011), resolution=(2560, 1440)))
    repeat_trial(crystal)
    touch(Template(r"tpl1610618247550.png", record_pos=(0.459, -0.252), resolution=(2560, 1440)))
    sleep(1)
    touch(Template(r"tpl1610618247550.png", record_pos=(0.459, -0.252), resolution=(2560, 1440)))
    sleep(1)
    return

def repeat_trial(times=10):
    sleep(1)
    touch(Template(r"tpl1610617954337.png", record_pos=(0.374, 0.217), resolution=(2560, 1440)))
    sleep(1)
    for i in range(times):
        try:
            touch(Template(r"tpl1610617997663.png", record_pos=(0.093, 0.23), resolution=(2560, 1440)))
            # TODO: handle no stamina
            sleep(1)
            touch(Template(r"tpl1610618017106.png", record_pos=(0.004, -0.117), resolution=(2560, 1440)))
            sleep(0.5)
        except:
            break
    if exists(Template(r"tpl1610619992857.png", record_pos=(0.001, 0.113), resolution=(2560, 1440))):
        touch(Template(r"tpl1610618083060.png", record_pos=(0.459, -0.253), resolution=(2560, 1440)))
    sleep(1)
    return
    
    