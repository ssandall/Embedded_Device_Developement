import RPi.GPIO as GPIO
import time

try:

    while 1:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.25)

except KeyboardInterrupt:
    GPIO.cleanup()
