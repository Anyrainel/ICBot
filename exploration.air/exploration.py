# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

def do_exploration(stage="2-4", times=10):
    touch(Template(r"tpl1610545774912.png", record_pos=(0.157, -0.004), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610545795013.png", record_pos=(-0.104, -0.015), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610545818179.png", record_pos=(-0.028, 0.064), resolution=(2560, 1440)))
    sleep(2)
    for i in range(times):
        farm_stage(stage)
    sleep(1)
    touch(Template(r"tpl1610545843875.png", record_pos=(0.461, -0.254), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610545843875.png", record_pos=(0.461, -0.254), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610545843875.png", record_pos=(0.461, -0.254), resolution=(2560, 1440)))
    sleep(1)
    return


def farm_stage(stage):
    touch(Template(r"tpl1610016403100.png", record_pos=(0.362, -0.041), resolution=(2560, 1440)))
    sleep(3)
    touch(Template(r"tpl1610016421424.png", record_pos=(0.389, 0.069), resolution=(2560, 1440)))
    sleep(3)
    if exists(Template(r"tpl1610017457434.png", record_pos=(-0.112, -0.148), resolution=(2560, 1440))):
        touch(Template(r"tpl1610017466492.png", record_pos=(0.097, 0.109), resolution=(2560, 1440)))
        sleep(2)
        touch(Template(r"tpl1610017480675.png", record_pos=(0.199, 0.084), resolution=(2560, 1440)))
        sleep(2)
        touch(p([0.924, 0.141]))
        sleep(2)
        touch(Template(r"tpl1610016421424.png", record_pos=(0.389, 0.069), resolution=(2560, 1440)))
        sleep(3)
    
    if exists(Template(r"tpl1610017457434.png", record_pos=(-0.112, -0.148), resolution=(2560, 1440))): # no stamina
        touch(Template(r"tpl1610546178455.png", record_pos=(0.459, -0.254), resolution=(2560, 1440)))
        touch(Template(r"tpl1610546178455.png", record_pos=(0.459, -0.254), resolution=(2560, 1440)))
        sleep(1)
        return
    try:
        touch(Template(r"tpl1610016448754.png", record_pos=(0.42, 0.226), resolution=(2560, 1440)))
    except: # no attempts left
        touch(Template(r"tpl1610546178455.png", record_pos=(0.459, -0.254), resolution=(2560, 1440)))
        sleep(1)
        return
    sleep(150)
    touch(Template(r"tpl1610016632778.png", record_pos=(0.096, 0.111), resolution=(2560, 1440)))
    touch(Template(r"tpl1610016650053.png", record_pos=(-0.111, 0.133), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610016669224.png", record_pos=(0.161, -0.194), resolution=(2560, 1440)))
    sleep(1)
    touch(Template(r"tpl1610016669224.png", record_pos=(0.161, -0.194), resolution=(2560, 1440)))
    sleep(3)
    return

