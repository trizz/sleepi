#!/usr/bin/python

import sys
import time

from modules import MovementDetection
from modules import WakeUp

wakeup = WakeUp.WakeUp('wakeup.slpi')
movement_detection = MovementDetection.MovementDetection()

def main_loop():
    while 1:
        # do your stuff... and wait a second.
        time.sleep(1)

if __name__ == '__main__':
    try:
        # Start the movement detection.
        movement_loop = movement_detection.detect_movement(True)
        wakeup.set_datetime('19870317', '1640')
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
