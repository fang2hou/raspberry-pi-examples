import RPi.GPIO as GPIO

LED_R = 17
LED_G = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

if __name__ == "__main__":
    try:
        while True:
            GPIO.output(LED_R, GPIO.HIGH)
            GPIO.output(LED_G, GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(6)
