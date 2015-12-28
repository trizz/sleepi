#!/usr/bin/python

import sys
import time

from modules import MovementDetection
from modules import WakeUp
from scripts import ledBar

led_bar = ledBar.ledBar()

wakeup = WakeUp.WakeUp(led_bar, 'wakeup.slpi')
movement_detection = MovementDetection.MovementDetection(led_bar)


def main_loop():
    while True:
        wakeup.check()
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        # Start the movement detection.
        movement_loop = movement_detection.detect_movement(True)
        wakeup.remove_old_items()
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
