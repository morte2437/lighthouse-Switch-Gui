#!/usr/bin/env python3

import logging


def initialise(debug):

    if debug:
        logging.basicConfig(
            filename='lighthouse-keeper.log',
            encoding='utf-8',
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s: %(message)s')
    else:
        logging.basicConfig(
            filename='lighthouse-keeper.log',
            encoding='utf-8',
            level=logging.WARNING,
            format='%(asctime)s %(levelname)s: %(message)s')


class Output():
    def __init__(self):
        self.debugMode = logging.debug

    def info(self, message):
        print(message)
        logging.info(message)

    def debug(self, message):
        if self.debugMode: print(message)
        logging.debug(message)

    def error(self, message):
        print("ERROR: " + message)
        logging.error(message)

    def exception(self, message):
        if self.debugMode: print(message)
        logging.exception(message)


output = Output()
