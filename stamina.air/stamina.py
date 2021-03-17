# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

def buy_stamina(times=5):
    touch(Template(r"tpl1610618401547.png", record_pos=(0.238, -0.246), resolution=(2560, 1440)))
    sleep(1)
    if exists(Template(r"tpl1610618896822.png", threshold=0.9, record_pos=(0.266, 0.129), resolution=(2560, 1440))):
        touch(p([0.945, 0.061]))
        sleep(1)
        return
    for i in range(times):
        touch(Template(r"tpl1610618435637.png", record_pos=(0.203, 0.086), resolution=(2560, 1440)))
        sleep(2)
    touch(p([0.945, 0.061]))
    sleep(1)
    return
