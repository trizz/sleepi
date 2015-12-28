import RPi.GPIO as GPIO
import time
import ledstrip
import async
import effects

# Initialize the ledstrip.
led = ledstrip.strand()

# GPIO pin of the PIR sensor.
sensor = 4

# Setup the GPIO.
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

# The number of seconds the ledstrip should be active when movement is detected.
defaultActiveTime = 5

# Remaining seconds before the ledstrip fades out.
remainingSeconds = 5

# Set default states for the app.
strip_active = False
stop_detection = False
show_log = False


def reset_timer(additional_seconds=0):
    global remainingSeconds, defaultActiveTime
    remainingSeconds = defaultActiveTime + additional_seconds


def log(msg):
    if show_log:
        print(msg)


def set_log(what):
    global show_log
    show_log = what


def set_stop_detection():
    global stop_detection
    stop_detection = True


# Use a decorator to run this function async to prevent blocking the app when fading in/out.
@async.run_async_daemon
def activate_ledstrip():
    global strip_active, remainingSeconds

    # Every time this function is called, movement is detected, so reset the timer (+1 addition second)
    reset_timer(1)

    # If the strip isn't active, set it active, fade in and countdown to a fade out.
    if not strip_active:
        strip_active = True
        effects.fade_in(led)

        # Sleep one second at a time until the remaining seconds reached zero. This can be reset by resetTimer().
        while remainingSeconds > 0:
            log("Remaining seconds: %s" % remainingSeconds)
            time.sleep(1)
            remainingSeconds -= 1

        effects.fade_out(led)
        strip_active = False


# Endless loop to detect movement by the PIR sensor, at least until stop_detection is changed to true.
@async.run_async_daemon
def detect_movement(write_log=False):
    global stop_detection
    set_log(write_log)
    previous_state = False
    current_state = False

    while not stop_detection:
        time.sleep(0.1)
        previous_state = current_state
        current_state = GPIO.input(sensor)
        if current_state != previous_state:
            new_state = "HIGH" if current_state else "LOW"
            log("GPIO pin %s is %s" % (sensor, new_state))

            if new_state == "HIGH":
                activate_ledstrip()

    effects.fade_out(led)
