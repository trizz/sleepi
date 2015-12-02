import time


def fade_in(led_bar):
    for i in xrange(4, 25):
        led_bar.fill((i * 10), (i * 10), (i * 10))
        time.sleep(0.05)


def fade_out(led_bar):
    for i in xrange(4, 25):
        led_bar.fill((250 - (i * 10)), (250 - (i * 10)), (250 - (i * 10)))
        time.sleep(0.05)
