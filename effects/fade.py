import time


class Fade:
    def __init__(self, led_bar):
        self.led_bar = led_bar

    def white_in(self):
        for brightness in [x * 0.01 for x in range(0, 100)]:
            self.led_bar.fillHSV(1, 0, brightness)
            time.sleep(0.01)

    def white_out(self):
        for i in xrange(4, 25):
            self.led_bar.fillRGB((250 - (i * 10)), (250 - (i * 10)), (250 - (i * 10)))
            time.sleep(0.05)