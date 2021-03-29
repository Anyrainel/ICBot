# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

def do_exploration(stage="2-4", rec_only=True, times=2):
    touch(Template(r"tpl1610545774912.png", record_pos=(0.157, -0.004), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610545795013.png", record_pos=(-0.104, -0.015), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610545818179.png", record_pos=(-0.028, 0.064), resolution=(2560, 1440)))
    sleep(2)
    for i in range(times):
        if not farm_stage(stage, rec_only):
            break
    sleep(1)
    back(3)
    sleep(1)
    return


def farm_stage(stage, rec_only):
    if rec_only:
        if stage == "2-4":
            if not exists(Template(r"tpl1616870851897.png", threshold=0.9, record_pos=(0.332, -0.114), resolution=(1920, 1080))):
                return False
        elif stage == "2-3":
            if not exists(Template(r"tpl1616870894675.png", threshold=0.9, record_pos=(0.151, 0.062), resolution=(1920, 1080))):
                return False
        elif stage == "2-2":
            pass
        elif stage == "2-1":
            if not exists(Template(r"tpl1616870945985.png", threshold=0.9, record_pos=(-0.093, 0.031), resolution=(1920, 1080))):
                return False
    if stage == "2-4":
        touch(Template(r"tpl1616871028978.png", record_pos=(0.346, -0.098), resolution=(1920, 1080)))
    elif stage == "2-3":
        touch(Template(r"tpl1616871053963.png", record_pos=(0.163, 0.079), resolution=(1920, 1080)))
    elif stage == "2-2":
        touch(Template(r"tpl1616871076813.png", record_pos=(0.133, -0.044), resolution=(1920, 1080)))
    elif stage == "2-1":
        touch(Template(r"tpl1616871114747.png", record_pos=(-0.05, 0.038), resolution=(1920, 1080)))
    auto_farm()
    return
    
    
def auto_farm():
    sleep(1)
    auto = exists(Template(r"tpl1616871208074.png", threshold=0.9, target_pos=4, record_pos=(0.364, 0.205), resolution=(1920, 1080)))
    if auto:
        touch(auto)
    touch(Template(r"tpl1610016421424.png", record_pos=(0.389, 0.069), resolution=(2560, 1440)))
    sleep(2)
    if exists(Template(r"tpl1610017457434.png", record_pos=(-0.112, -0.148), resolution=(2560, 1440))):
        touch(Template(r"tpl1610017466492.png", record_pos=(0.097, 0.109), resolution=(2560, 1440)))
        sleep(1)
        touch(Template(r"tpl1610017480675.png", record_pos=(0.199, 0.084), resolution=(2560, 1440)))
        sleep(2)
        touch(p([0.924, 0.141]))
        sleep(2)
        touch(Template(r"tpl1610016421424.png", record_pos=(0.389, 0.069), resolution=(2560, 1440)))
        sleep(2)
    if exists(Template(r"tpl1610017457434.png", record_pos=(-0.112, -0.148), resolution=(2560, 1440))): # no stamina
        back(2)
        return
    try:
        touch(Template(r"tpl1610016448754.png", record_pos=(0.42, 0.226), resolution=(2560, 1440)))
    except: # no attempts left
        back(1)
        return
    sleep(150)
    touch(Template(r"tpl1610016632778.png", record_pos=(0.096, 0.111), resolution=(2560, 1440)))
    touch(Template(r"tpl1610016650053.png", record_pos=(-0.111, 0.133), resolution=(2560, 1440)))
    sleep(2)
    touch(Template(r"tpl1610016669224.png", record_pos=(0.161, -0.194), resolution=(2560, 1440)))
    sleep(1)
    touch(Template(r"tpl1610016669224.png", record_pos=(0.161, -0.194), resolution=(2560, 1440)))
    sleep(2)
    return

def back(times):
    for _ in range(times):
        
        touch(Template(r"tpl1610545843875.png", record_pos=(0.461, -0.254), resolution=(2560, 1440)))
        sleep(1)
    return