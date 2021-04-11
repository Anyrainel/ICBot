# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

extra = 2

def do_dates(partners=[], extra_click=2):
    global extra
    extra = extra_click
    touch(Template(r"tpl1610822318286.png", record_pos=(-0.458, -0.009), resolution=(2560, 1440)))
    for partner in partners:
        sleep(1)
        if eval(partner + '()'):
            back(2)
    back(1)
    sleep(1)
    return

def saya():
    if not touch_partner(0, [Template(r"tpl1616169489812.png", record_pos=(-0.109, -0.027), resolution=(2560, 1440)), Template(r"tpl1616169290387.png", record_pos=(-0.109, -0.031), resolution=(2560, 1440))]):
        return False
    if not start_date(4):
        return True
    if exists(Template(r"tpl1616165561978.png", threshold=0.8, record_pos=(-0.007, 0.007), resolution=(2560, 1440))):
        converse(choices=[2,1,2,2,1],talks=[7,8,7,7,11])
    elif exists(Template(r"tpl1616325846715.png", record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,1,1,1,1],talks=[5,6,6,4,6])
    elif exists(Template(r"tpl1616325763192.png", record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,1,1],talks=[7,6,6,9,8])
    return True
    
def nina():
    if not touch_partner(0, [Template(r"tpl1616169304283.png", record_pos=(0.024, -0.027), resolution=(2560, 1440)), Template(r"tpl1616169501169.png", record_pos=(0.02, -0.028), resolution=(2560, 1440))]):
        return False
    if not start_date(3):
        return True
    if exists(Template(r"tpl1616165832886.png", threshold=0.8, record_pos=(-0.029, -0.012), resolution=(2560, 1440))):
        converse(choices=[2,1,2,2,1],talks=[10,7,7,8,6])
    elif exists(Template(r"tpl1616165908673.png", threshold=0.8, record_pos=(-0.007, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,2,1,1,1],talks=[5,5,6,5,13])
    elif exists(Template(r"tpl1616165672458.png", threshold=0.8, record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,1,1],talks=[6,5,5,5,5])
    return True

def victoria():
    if not touch_partner(0, [Template(r"tpl1616169314308.png", record_pos=(0.154, -0.031), resolution=(2560, 1440))]):
        return False
    if not start_date(5):
        return True
    if exists(Template(r"tpl1616166056754.png", threshold=0.8, record_pos=(-0.009, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,2,1],talks=[8,6,7,6,11])
    elif exists(Template(r"tpl1616166124222.png", threshold=0.8, record_pos=(-0.008, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,1,1,1,1],talks=[7,5,5,2,8])
    elif exists(Template(r"tpl1616166348477.png", threshold=0.8, record_pos=(-0.009, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,2,1,1,1],talks=[4,5,8,3,8])
    return True

def jasmine():
    if not touch_partner(0, [Template(r"tpl1610822342992.png", record_pos=(0.155, 0.148), resolution=(2560, 1440))]):
        return False
    if not start_date(3):
        return True
    if exists(Template(r"tpl1610821646664.png", threshold=0.8, record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,2,2], talks=[5,5,6,6,6])
    elif exists(Template(r"tpl1611510161734.png", threshold=0.8, record_pos=(-0.005, 0.006), resolution=(2560, 1440))):
        converse(choices=[2,1,1,1,1], talks=[3,4,5,6,5])
    elif exists(Template(r"tpl1611071428403.png", threshold=0.8, record_pos=(-0.004, -0.094), resolution=(2560, 1440))):
        converse(choices=[1,2,1,1,1], talks=[4,3,6,4,6])
    return True

def polly():
    if not touch_partner(0, [Template(r"tpl1616169701430.png", record_pos=(0.153, 0.194), resolution=(2560, 1440)), Template(r"tpl1616169460778.png", record_pos=(0.155, 0.193), resolution=(2560, 1440))]):
        return False
    if not start_date(3):
        return True
    if exists(Template(r"tpl1617080456478.png", threshold=0.8, record_pos=(-0.004, -0.093), resolution=(2560, 1440))):
        converse(choices=[1,2,1,2,1],talks=[4,4,4,5,6])
    elif exists(Template(r"tpl1616166687036.png", threshold=0.8, record_pos=(-0.005, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,2,2,1,1],talks=[4,3,7,5,6])
    elif exists(Template(r"tpl1616166584098.png", threshold=0.8, record_pos=(-0.038, -0.111), resolution=(2560, 1440))):
        converse(choices=[1,1,1,2,2],talks=[7,5,4,4,6])
    return True

def alice():
    if not touch_partner(0, [Template(r"tpl1610822524231.png", record_pos=(0.027, 0.195), resolution=(2560, 1440))]):
        return False
    if not start_date(3):
        return True
    if exists(Template(r"tpl1610822631093.png", threshold=0.85, record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,1,2,1], talks=[6,5,6,6,4])
    elif exists(Template(r"tpl1611024321102.png", threshold=0.8, record_pos=(-0.004, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,1,2,1,1], talks=[6,5,6,6,7])
    elif exists(Template(r"tpl1610898386748.png", threshold=0.8, record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,1,2,1,2], talks=[5,6,5,5,6])
    return True

def kiraya():
    if not touch_partner(1, [Template(r"tpl1616686124448.png", record_pos=(0.021, 0.143), resolution=(1920, 1080)), Template(r"tpl1616686161109.png", record_pos=(0.022, 0.148), resolution=(1920, 1080))]):
        return False
    if not start_date(6):
        return True
    if exists(Template(r"tpl1616748433527.png", threshold=0.8, record_pos=(-0.005, -0.094), resolution=(1920, 1080))):
        converse(choices=[1,1,1,1,2], talks=[5,3,5,7,8])
    elif exists(Template(r"tpl1616755064937.png", threshold=0.8, record_pos=(-0.002, -0.095), resolution=(1920, 1080))):
        converse(choices=[1,1,1,2,2], talks=[5,11,5,8,3])
    elif exists(Template(r"tpl1617080173533.png", threshold=0.8, record_pos=(-0.003, -0.093), resolution=(2560, 1440))):
        converse(choices=[1,1,1,1,1], talks=[2,8,4,7,5])
    return True

def yuffie():
    if not touch_partner(4, [Template(r"tpl1616169629826.png", record_pos=(-0.109, -0.026), resolution=(2560, 1440)), Template(r"tpl1616169530971.png", record_pos=(-0.108, -0.03), resolution=(2560, 1440))]):
        return False
    if not start_date(3):
        return True
    if exists(Template(r"tpl1616755286363.png", threshold=0.8, record_pos=(-0.005, 0.005), resolution=(1920, 1080))):
        converse(choices=[2,1,1,2,2],talks=[5,6,6,5,5])
    elif exists(Template(r"tpl1616167146896.png", threshold=0.8, record_pos=(-0.007, 0.004), resolution=(2560, 1440))):
        converse(choices=[2,1,1,1,1],talks=[4,6,5,5,5])
    elif exists(Template(r"tpl1616326076878.png", record_pos=(-0.004, -0.093), resolution=(2560, 1440))):
        converse(choices=[1,1,1,1,2],talks=[5,5,4,4,5])
    return True

def flora():
    success = touch_partner(4, [Template(r"tpl1610823098904.png", record_pos=(0.156, 0.148), resolution=(2560, 1440)), Template(r"tpl1616168630228.png", record_pos=(0.285, 0.136), resolution=(2560, 1440))])
    if not success:
        return False
    if not start_date(4):
        return True
    if exists(Template(r"tpl1611071759293.png", threshold=0.8, record_pos=(-0.004, -0.095), resolution=(2560, 1440))):
        converse(choices=[1,1,1,1,1], talks=[6,6,5,6,6])
    elif exists(Template(r"tpl1610823186572.png", threshold=0.8, record_pos=(-0.004, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,2,2,2], talks=[3,10,5,4,7])
    elif exists(Template(r"tpl1610898635528.png", threshold=0.8, record_pos=(-0.007, -0.093), resolution=(2560, 1440))):
        converse(choices=[1,2,2,1,1], talks=[7,4,3,6,6])
    return True

def fenebeth():
    if not touch_partner(5, [Template(r"tpl1616169608359.png", record_pos=(0.283, -0.026), resolution=(2560, 1440)), Template(r"tpl1616169554233.png", record_pos=(0.286, -0.028), resolution=(2560, 1440))]):
        return False
    if not start_date(3):
        return True
    if exists(Template(r"tpl1616167514720.png", threshold=0.8, record_pos=(-0.004, 0.006), resolution=(2560, 1440))):
        converse(choices=[2,2,2,2,1],talks=[4,5,4,4,5])
    elif exists(Template(r"tpl1616167597702.png", threshold=0.8, record_pos=(-0.006, -0.094), resolution=(2560, 1440))):
        converse(choices=[1,2,2,2,2],talks=[6,4,6,6,6])
    elif exists(Template(r"tpl1616316491036.png", record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,2,2,1,1],talks=[5,5,5,4,5])
    return True

def frantiva():
    if not touch_partner(5, [Template(r"tpl1618100844295.png", record_pos=(0.022, 0.143), resolution=(2560, 1440)), Template(r"tpl1618101069392.png", record_pos=(0.022, 0.142), resolution=(2560, 1440))]):
        return False
    if not start_date(3):
        return True
    if False: # Does the sound of the horn mean anything?
        converse(choices=[2,2,1,2,1],talks=[4,6,6,6,5])
    elif exists(Template(r"tpl1618100960220.png", record_pos=(-0.005, 0.005), resolution=(2560, 1440))):
        converse(choices=[2,1,2,1,1],talks=[4,5,3,5,5])
    elif False: # Why have you come here?
        converse(choices=[2,1,2,1,2],talks=[4,4,4,4,4])
    return True

def ashwaya():
    if not touch_partner(5, [Template(r"tpl1616167967941.png", record_pos=(0.285, 0.141), resolution=(2560, 1440))]):
        return False
    if not start_date(3):
        return True
    if exists(Template(r"tpl1616165334099.png", threshold=0.8, record_pos=(-0.004, -0.093), resolution=(2560, 1440))):
        converse(choices=[1,2,1,2,1],talks=[4,4,5,3,3])
    elif exists(Template(r"tpl1616165007182.png", threshold=0.8, record_pos=(-0.006, -0.092), resolution=(2560, 1440))):
        converse(choices=[1,2,2,2,1],talks=[5,6,5,4,3])
    elif exists(Template(r"tpl1616164492748.png", threshold=0.8, record_pos=(-0.009, -0.096), resolution=(2560, 1440))):
        converse(choices=[1,2,2,2,2],talks=[5,6,5,4,4])
    return True

def converse(choices=[], talks=[]):
    if not talks:
        talks = [10] * 5
    for i in range(5):
        if choices[i] == 1:
            touch(p([0.504, 0.337]))
        elif choices[i] == 2:
            touch(p([0.504, 0.51]))
        sleep(0.5)
        talk(talks[i])
    talk(0) # extra talk
    sleep(3)
    return

def talk(times):
    for _ in range(times * 2 + extra):
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
