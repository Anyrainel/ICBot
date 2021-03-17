# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *

auto_setup(__file__)

def do_dates():
    touch(Template(r"tpl1610822318286.png", record_pos=(-0.458, -0.009), resolution=(2560, 1440)))
    do_jasmine()
    do_alice()
    do_flora()
    back(1)
    return

def do_jasmine():
    sleep(1)
    swipe([1586, 1282], vector=[0.0098, -0.6318])
    touch(Template(r"tpl1610822342992.png", record_pos=(0.155, 0.148), resolution=(2560, 1440)))
    start_date()
    talk(15)
    if exists(Template(r"tpl1610821646664.png", threshold=0.8, record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,2,2], talks=[12,12,12,12,12])
    elif exists(Template(r"tpl1611071428403.png", threshold=0.8, record_pos=(-0.004, -0.094), resolution=(2560, 1440))):
        converse(choices=[1,2,1,1,1], talks=[10,10,12,10,12])
    elif exists(Template(r"tpl1611510161734.png", threshold=0.8, record_pos=(-0.005, 0.006), resolution=(2560, 1440))):
        converse(choices=[2,1,1,1,1], talks=[10,10,10,12,12])
    sleep(3)
    back(2)
    return

def do_alice():
    sleep(1)
    swipe([1586, 1282], vector=[0.0098, -0.6318])
    touch(Template(r"tpl1610822524231.png", record_pos=(0.027, 0.195), resolution=(2560, 1440)))
    start_date()
    talk(10)
    if exists(Template(r"tpl1611024321102.png", threshold=0.8, record_pos=(-0.004, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,1,2,1,1], talks=[12,12,12,12,16])
    elif exists(Template(r"tpl1610898386748.png", threshold=0.8, record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,1,2,1,2], talks=[10,13,10,10,14])
    elif exists(Template(r"tpl1610822631093.png", threshold=0.85, record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,2,1], talks=[16,12,14,14,14])
    sleep(3)
    back(2)
    return


def do_flora():
    touch(Template(r"tpl1610823081889.png", record_pos=(0.453, 0.154), resolution=(2560, 1440)))
    sleep(0.5)
    touch(Template(r"tpl1610823098904.png", record_pos=(0.156, 0.148), resolution=(2560, 1440)))
    start_date()
    talk(10)
    if exists(Template(r"tpl1610823186572.png", threshold=0.8, record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,2,2,2], talks=[10,20,12,10,14])
    elif exists(Template(r"tpl1611071759293.png", threshold=0.8, record_pos=(-0.004, -0.095), resolution=(2560, 1440))):
        converse(choices=[1,1,1,1,1], talks=[14,12,12,12,12])
    elif exists(Template(r"tpl1610898635528.png", threshold=0.8, record_pos=(-0.007, -0.093), resolution=(2560, 1440))):
        converse(choices=[1,2,2,1,1], talks=[14,10,10,12,12])
    sleep(3)
    back(2)
    return

def converse(choices=[], talks=[]):
    for i in range(5):
        choose(choices[i])
        talk(talks[i])
    return

def choose(choice):
    if choice == 1:
        touch([1286, 484])
    elif choice == 2:
        touch([1339, 753])
    sleep(0.5)
    return

def talk(times):
    for _ in range(times):
        touch([1436, 1154])
        sleep(0.3)
    return

def start_date():
    sleep(1)
    touch(Template(r"tpl1610822365239.png", record_pos=(0.416, 0.01), resolution=(2560, 1440)))
    sleep(0.5)
    touch(Template(r"tpl1610822385446.png", record_pos=(0.001, -0.077), resolution=(2560, 1440)))
    sleep(2)
    return

def back(times=2):
    for _ in range(times):
        touch(Template(r"tpl1610822189335.png", record_pos=(0.46, -0.254), resolution=(2560, 1440)))
        sleep(0.5)
    return
