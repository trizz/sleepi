import time


class Fade:
    def __init__(self, led_bar):
        self.led_bar = led_bar

    def fade_in(self):
        for i in xrange(4, 25):
            self.led_bar.fill((i * 10), (i * 10), (i * 10))
            time.sleep(0.05)

    def fade_out(self):
        for i in xrange(4, 25):
            self.led_bar.fill((250 - (i * 10)), (250 - (i * 10)), (250 - (i * 10)))
            time.sleep(0.05)
