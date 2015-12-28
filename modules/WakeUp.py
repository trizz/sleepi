#!/usr/bin/env python

import json
from time import strftime


class WakeUp:

    def __init__(self, config_file="wakeup.slpi"):
        self.config = dict
        self.configFile = config_file
        self.get_data()

    def get_data(self):
        with open(self.configFile, 'r') as f:
            self.config = json.load(f)

    def set_datetime(self, date, time, duration=600, effect="sunrise", repeat=None):
        self.config[date+time] = {'duration': duration, 'effect': effect, 'repeat': repeat}
        with open(self.configFile, 'w') as f:
            json.dump(self.config, f)

    def remove_old_items(self):
        now = strftime("%Y%m%d%H%M")
        keys = self.config.keys()
        for key in keys:
            if key < now:
                # Only delete when it isn't a repeating one.
                if self.config[key]['repeat'] is None:
                    del self.config[key]
