# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
using("common.air")
from common import *

def do_arena(times=50):
    if times == 0:
        return
    touch(Template(r"arena.png", record_pos=(0.273, -0.034), resolution=(2560, 1440)))
    sleep(1)
    while not exists(Template(r"tpl1615997899077.png", record_pos=(-0.397, -0.255), resolution=(2560, 1440))):
        touch(Template(r"dream.png", record_pos=(-0.216, 0.003), resolution=(2560, 1440)))
    sleep(1)
    fight(times)
    sleep(1)
    touch(Template(r"back1.png", record_pos=(0.461, -0.254), resolution=(2560, 1440)))
    while not exists(Template(r"arena.png", record_pos=(0.273, -0.034), resolution=(2560, 1440))):
        touch(Template(r"back1.png", record_pos=(0.461, -0.254), resolution=(2560, 1440)))
    sleep(1)
    return


def fight(times=50):
    # get through new season
    touch(p([0.509, 0.708]))
    sleep(0.5)
    touch(p([0.509, 0.708]))
    if exists(Template(r"0_50.png", threshold=0.9, record_pos=(-0.36, 0.248), resolution=(2560, 1440))):
        return
    opponents = [
        p([0.131, 0.301]), p([0.321, 0.294]), p([0.496, 0.301]), p([0.688, 0.307]), p([0.877, 0.301]),
        p([0.13, 0.545]), p([0.316, 0.548]), p([0.491, 0.548]), p([0.673, 0.548]), p([0.866, 0.535]),
    ]
    current = 0
    record = 0
    while record < times:
        record += 1
        touch(p([0.509, 0.708])) # get through Congrats screen
        sleep(1)
        # find opponent
        while current < 10:
            touch(opponents[current])
            sleep(0.5)
            fast = exists(Template(r"fast_challenge.png", record_pos=(0.181, 0.156), resolution=(2560, 1440)))
            if fast:
                touch(fast)
                break
            else:
                current += 1
        # Error, no opponent found
        if current == 10:
            break
        # Try until win
        while True:
            if exists(Template(r"fast_challenge.png", threshold=0.8, record_pos=(0.181, 0.156), resolution=(2560, 1440))): # No tickets left
                touch(Template(r"back2.png", record_pos=(0.277, -0.18), resolution=(2560, 1440)))
                return
            elif exists(Template(r"victory.png", record_pos=(-0.001, -0.156), resolution=(2560, 1440))):
                sleep(0.5)
                touch(Template(r"confirm2.png", record_pos=(-0.0, 0.205), resolution=(2560, 1440)))
                sleep(2)
                break
            else:
#             elif exists(Template(r"failure.png", record_pos=(-0.006, -0.157), resolution=(2560, 1440))):
                touch(Template(r"confirm1.png", record_pos=(-0.122, 0.099), resolution=(2560, 1440)))
                sleep(1.5)
                touch(opponents[current])
                sleep(1)
                touch(Template(r"fast_challenge.png", record_pos=(0.181, 0.156), resolution=(2560, 1440)))
        current = (current + 1) % 10
    return
            
