import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number
GPIO.setmode(GPIO.BCM)
led_pin = 12

# Set up the GPIO pin for output
GPIO.setup(led_pin, GPIO.OUT)

try:
    start_time = time.time()

    while (time.time() - start_time) < 10:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.5)  # LED on for 0.5 seconds

        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)  # LED off for 0.5 seconds

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()
