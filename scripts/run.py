#!/usr/bin/python

import sys
import time
import movement


def main_loop():
    while 1:
        # do your stuff... and wait a second.
        time.sleep(1)

if __name__ == '__main__':
    try:
        # Start the movement detection.
        movement_loop = movement.detect_movement(True)
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
