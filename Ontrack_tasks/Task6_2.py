import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)

    while 1:
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.25)

except KeyboardInterrupt:
    GPIO.cleanup()
