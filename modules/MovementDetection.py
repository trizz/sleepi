import RPi.GPIO as GPIO
import time
from scripts import async, effects


class MovementDetection:
    def __init__(self, led_bar):
        # Initialize the ledstrip.
        self.led_bar = led_bar

        # GPIO pin of the PIR sensor.
        self.sensor = 4

        # Setup the GPIO.
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor, GPIO.IN, GPIO.PUD_DOWN)

        # The number of seconds the ledstrip should be active when movement is detected.
        self.defaultActiveTime = 5

        # Remaining seconds before the ledstrip fades out.
        self.remainingSeconds = 5

        # Set default states for the app.
        self.strip_active = False
        self.stop_detection = False
        self.show_log = False

    def reset_timer(self, additional_seconds=0):
        self.remainingSeconds = self.defaultActiveTime + additional_seconds

    def log(self, msg):
        if self.show_log:
            print(msg)

    def set_log(self, what):
        self.show_log = what

    def set_stop_detection(self):
        self.stop_detection = True

    # Use a decorator to run this function async to prevent blocking the app when fading in/out.
    @async.run_async_daemon
    def activate_ledstrip(self):

        # Every time this function is called, movement is detected, so reset the timer (+1 addition second)
        self.reset_timer(1)

        # If the strip isn't active, set it active, fade in and countdown to a fade out.
        if not self.strip_active:
            self.strip_active = True
            effects.fade_in(self.led_bar)

            # Sleep one second at a time until the remaining seconds reached zero. This can be reset by resetTimer().
            while self.remainingSeconds > 0:
                self.log("Remaining seconds: %s" % self.remainingSeconds)
                time.sleep(1)
                self.remainingSeconds -= 1

            effects.fade_out(self.led_bar)
            self.strip_active = False

    # Endless loop to detect movement by the PIR sensor, at least until stop_detection is changed to true.
    @async.run_async_daemon
    def detect_movement(self, write_log=False):
        self.set_log(write_log)
        previous_state = False
        current_state = False

        while not self.stop_detection:
            time.sleep(0.1)
            previous_state = current_state
            current_state = GPIO.input(self.sensor)
            if current_state != previous_state:
                new_state = "HIGH" if current_state else "LOW"
                self.log("GPIO pin %s is %s" % (self.sensor, new_state))

                if new_state == "HIGH":
                    self.activate_ledstrip()

        effects.fade_out(self.led_bar)
