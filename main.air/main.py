# -*- encoding=utf8 -*-
__author__ = "Anyrainel"

from airtest.core.api import *
from pathlib import Path
import os, json, logging

auto_setup(__file__)

ST.PROJECT_ROOT = Path(__file__).parent.parent.absolute()
ST.OPDELAY = 0.2
ST.FIND_TIMEOUT_TMP = 2
ST.FIND_TIMEOUT = 5

using("arena.air")
using("ares.air")
using("common.air")
using("expedition.air")
using("exploration.air")
using("quest.air")
using("stamina.air")
using("trial.air")

import arena, ares, common, expedition, exploration, quest, stamina, trial

def main():
    sequence, logger = init()
    for task in sequence:
        action = task['Action']
        args = task['Args']
        logger.error(">>>> Starting Action %s <<<<", action)
        if action == 'arena':
            arena.do_arena(**args)
        elif action == 'ares':
            ares.do_ares(**args)
        elif action == 'expedition':
            expedition.do_expedition(**args)
        elif action == 'exploration':
            exploration.do_exploration(**args)
        elif action == 'quest':
            quest.do_quest(**args)
        elif action == 'stamina':
            stamina.buy_stamina(**args)
        elif action == 'trial':
            trial.do_trials(**args)
        logger.error(">>>> Finished Action %s <<<<", action)
    return

def init():
    common.init_resolution()
    with open(os.path.join(ST.PROJECT_ROOT, 'settings.jsonc'), 'r') as txt:
        builder = ""
        for linestr in txt.readlines():
            line = linestr.strip()
            if not line.startswith('//'):
                builder += line
        setting = json.loads(builder)
    levels = {
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
    }
    logger = logging.getLogger("airtest")
    logger.setLevel(levels[setting['LoggingLevel']])
    return setting['BotSequence'], logger


main()

