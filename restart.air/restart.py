# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *

auto_setup(__file__)

stop_app('com.superprism.illusion')
sleep(2)
start_app('com.superprism.illusion')
sleep(10)
touch(Template(r"tpl1616166390582.png", record_pos=(-0.0, 0.179), resolution=(2560, 1440)))
sleep(15)

touch(Template(r"tpl1616166314073.png", record_pos=(0.396, -0.218), resolution=(2560, 1440)))
sleep(1)