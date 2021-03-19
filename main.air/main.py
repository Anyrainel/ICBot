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
using("date.air")
using("expedition.air")
using("exploration.air")
using("quest.air")
using("stamina.air")
using("trial.air")

import arena, ares, common, date, expedition, exploration, quest, stamina, trial

def init_logger(logger):
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        fmt='[%(asctime)s][%(levelname)s]<%(name)s> %(message)s',
        datefmt='%I:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def main():
    sequence, logger = init()
    for task in sequence:
        action = task['Action']
        args = task['Args']
        logger.info("==== Starting Action [%s] ====", action)
        logger.info("Args: %s" % args)
        if action == 'arena':
            arena.do_arena(**args)
        elif action == 'ares':
            ares.do_ares(**args)
        elif action == 'date':
            date.do_dates(**args)
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
        logger.info("==== Finished Action [%s] ====", action)
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
    airtestLogger = logging.getLogger("airtest")
    airtestLogger.setLevel(levels[setting['AirtestLoggingLevel']])
    logger = logging.getLogger('ICBot')
    init_logger(logger)
    return setting['BotSequence'], logger


main()

