import RPi.GPIO as GPIO
import time

# Pin Configuration
TRIG = 31  # GPIO pin for TRIG
ECHO = 29  # GPIO pin for ECHO
LED = 40   # GPIO pin for LED

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def measure_distance():
    # Trigger the ultrasonic sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10 microseconds pulse
    GPIO.output(TRIG, False)

    # Measure the time for echo
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Calculate distance
    duration = end_time - start_time
    distance = (duration * 34300) / 2  # Speed of sound = 343 m/s
    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")

        # Turn on LED if distance is below threshold (e.g., 10 cm)
        if dist < 10:
            GPIO.output(LED, True)
        else:
            GPIO.output(LED, False)

        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
