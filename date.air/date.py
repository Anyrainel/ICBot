# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

def do_dates(partners=[]):
    touch(Template(r"tpl1610822318286.png", record_pos=(-0.458, -0.009), resolution=(2560, 1440)))
    for partner in partners:
        sleep(1)
        if eval(partner + '()'):
            back(2)
    back(1)
    return

def saya():
    if not touch_partner(0, [Template(r"tpl1616169489812.png", record_pos=(-0.109, -0.027), resolution=(2560, 1440)), Template(r"tpl1616169290387.png", record_pos=(-0.109, -0.031), resolution=(2560, 1440))]):
        return False
    if not start_date(10):
        return True
    if exists(Template(r"tpl1616165561978.png", threshold=0.8, record_pos=(-0.007, 0.007), resolution=(2560, 1440))):
        converse(choices=[2,1,2,2,1])
    return True
    
def nina():
    if not touch_partner(0, [Template(r"tpl1616169304283.png", record_pos=(0.024, -0.027), resolution=(2560, 1440)), Template(r"tpl1616169501169.png", record_pos=(0.02, -0.028), resolution=(2560, 1440))]):
        return False
    if not start_date(10):
        return True
    if exists(Template(r"tpl1616165832886.png", threshold=0.8, record_pos=(-0.029, -0.012), resolution=(2560, 1440))):
        converse(choices=[2,1,2,2,1])
    elif exists(Template(r"tpl1616165672458.png", threshold=0.8, record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,1,1])
    elif exists(Template(r"tpl1616165908673.png", threshold=0.8, record_pos=(-0.007, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,2,1,1,1])
    return True

def victoria():
    if not touch_partner(0, [Template(r"tpl1616169314308.png", record_pos=(0.154, -0.031), resolution=(2560, 1440))]):
        return False
    if not start_date(10):
        return True
    if exists(Template(r"tpl1616166056754.png", threshold=0.8, record_pos=(-0.009, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,2,1])
    elif exists(Template(r"tpl1616166124222.png", threshold=0.8, record_pos=(-0.008, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,1,1,1,1])
    elif exists(Template(r"tpl1616166348477.png", threshold=0.8, record_pos=(-0.009, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,2,1,1,1])
    return True

def jasmine():
    if not touch_partner(0, [Template(r"tpl1610822342992.png", record_pos=(0.155, 0.148), resolution=(2560, 1440))]):
        return False
    if not start_date(15):
        return True
    if exists(Template(r"tpl1610821646664.png", threshold=0.8, record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,2,2], talks=[12,12,12,12,12])
    elif exists(Template(r"tpl1611071428403.png", threshold=0.8, record_pos=(-0.004, -0.094), resolution=(2560, 1440))):
        converse(choices=[1,2,1,1,1], talks=[10,10,12,10,12])
    elif exists(Template(r"tpl1611510161734.png", threshold=0.8, record_pos=(-0.005, 0.006), resolution=(2560, 1440))):
        converse(choices=[2,1,1,1,1], talks=[10,10,10,12,12])
    return True

def polly():
    if not touch_partner(0, [Template(r"tpl1616169701430.png", record_pos=(0.153, 0.194), resolution=(2560, 1440)), Template(r"tpl1616169460778.png", record_pos=(0.155, 0.193), resolution=(2560, 1440))]):
        return False
    if not start_date(10):
        return True
    if exists(Template(r"tpl1616166584098.png", threshold=0.8, record_pos=(-0.038, -0.111), resolution=(2560, 1440))):
        converse(choices=[2,2,2,1,1])
    elif exists(Template(r"tpl1616166687036.png", threshold=0.8, record_pos=(-0.005, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,2,2,1,1])
    return True

def alice():
    if not touch_partner(0, [Template(r"tpl1610822524231.png", record_pos=(0.027, 0.195), resolution=(2560, 1440))]):
        return False
    if not start_date(10):
        return True
    if exists(Template(r"tpl1611024321102.png", threshold=0.8, record_pos=(-0.004, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,1,2,1,1], talks=[12,12,12,12,16])
    elif exists(Template(r"tpl1610898386748.png", threshold=0.8, record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,1,2,1,2], talks=[10,13,10,10,14])
    elif exists(Template(r"tpl1610822631093.png", threshold=0.85, record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,2,1], talks=[16,12,14,14,14])
    return True

def yuffie():
    if not touch_partner(4, [Template(r"tpl1616169629826.png", record_pos=(-0.109, -0.026), resolution=(2560, 1440)), Template(r"tpl1616169530971.png", record_pos=(-0.108, -0.03), resolution=(2560, 1440))]):
        return False
    if not start_date(10):
        return True
    if exists(Template(r"tpl1616167146896.png", threshold=0.8, record_pos=(-0.007, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,1,1,1,1])
    return True

def flora():
    success = touch_partner(4, [Template(r"tpl1610823098904.png", record_pos=(0.156, 0.148), resolution=(2560, 1440)), Template(r"tpl1616168630228.png", record_pos=(0.285, 0.136), resolution=(2560, 1440))])
    if not success:
        return False
    if not start_date(10):
        return True
    if exists(Template(r"tpl1610823186572.png", threshold=0.8, record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,2,2,2], talks=[10,20,12,10,14])
    elif exists(Template(r"tpl1611071759293.png", threshold=0.8, record_pos=(-0.004, -0.095), resolution=(2560, 1440))):
        converse(choices=[1,1,1,1,1], talks=[14,12,12,12,12])
    elif exists(Template(r"tpl1610898635528.png", threshold=0.8, record_pos=(-0.007, -0.093), resolution=(2560, 1440))):
        converse(choices=[1,2,2,1,1], talks=[14,10,10,12,12])
    return True

def fenebeth():
    if not touch_partner(5, [Template(r"tpl1616169608359.png", record_pos=(0.283, -0.026), resolution=(2560, 1440)), Template(r"tpl1616169554233.png", record_pos=(0.286, -0.028), resolution=(2560, 1440))]):
        return False
    if not start_date(15):
        return True
    if exists(Template(r"tpl1616167514720.png", threshold=0.8, record_pos=(-0.004, 0.006), resolution=(2560, 1440))):
        converse(choices=[2,2,2,2,1])
    elif exists(Template(r"tpl1616167597702.png", threshold=0.8, record_pos=(-0.006, -0.094), resolution=(2560, 1440))):
        converse(choices=[1,2,2,2,2])
    return True

def ashwaya():
    if not touch_partner(5, [Template(r"tpl1616167967941.png", record_pos=(0.285, 0.141), resolution=(2560, 1440))]):
        return False
    if not start_date(10):
        return True
    if exists(Template(r"tpl1616165334099.png", threshold=0.8, record_pos=(-0.004, -0.093), resolution=(2560, 1440))):
        converse(choices=[1,2,1,2,1])
    elif exists(Template(r"tpl1616165007182.png", threshold=0.8, record_pos=(-0.006, -0.092), resolution=(2560, 1440))):
        converse(choices=[1,2,2,2,1])
    elif exists(Template(r"tpl1616164492748.png", threshold=0.8, record_pos=(-0.009, -0.096), resolution=(2560, 1440))):
        converse(choices=[1,2,2,2,2])
    return True

def converse(choices=[], talks=[]):
    if not talks:
        talks = [20, 20, 20, 20, 20]
    for i in range(5):
        # choose
        if choices[i] == 1:
            touch(p([0.504, 0.337]))
        elif choices[i] == 2:
            touch(p([0.504, 0.51]))
        sleep(0.5)
        talk(talks[i])
    sleep(3)
    return

def talk(times):
    for _ in range(times):
        touch(p([0.53, 0.84]))
        sleep(0.3)
    return

def touch_partner(fid, tpls):
    factions = [p([0.946, 0.228]), p([0.947, 0.349]), p([0.947, 0.491]), p([0.951, 0.654]), p([0.946, 0.783]), p([0.953, 0.921])]
    sleep(0.5)
    touch(factions[fid])
    sleep(1)
    for tpl in tpls:
        button = exists(tpl)
        if button:
            touch(button)
            return True
    swipe(p([0.592, 0.917]), vector=[0.0058, -0.6318])
    for tpl in tpls:
        button = exists(tpl)
        if button:
            touch(button)
            return True
    return False

def start_date(talk_times=10):
    sleep(1)
    touch(Template(r"tpl1610822365239.png", record_pos=(0.416, 0.01), resolution=(2560, 1440)))
    sleep(0.5)
    touch(Template(r"tpl1610822385446.png", record_pos=(0.001, -0.077), resolution=(2560, 1440)))
    sleep(2)
    if exists(Template(r"tpl1610822385446.png", record_pos=(0.001, -0.077), resolution=(2560, 1440))):
        return False
    talk(talk_times)
    return True

def back(times=2):
    for _ in range(times):
        touch(Template(r"tpl1610822189335.png", record_pos=(0.46, -0.254), resolution=(2560, 1440)))
        sleep(0.5)
    return
