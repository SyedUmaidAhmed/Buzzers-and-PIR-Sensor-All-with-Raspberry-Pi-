from gpiozero import MotionSensor, LED
import time
pir = MotionSensor(4)
led = LED(17)
print("Waiting for the sensor to settle")

pir.wait_for_no_motion()
while True:
    led.off()
    print("Ready")
    pir.wait_for_motion()
    led.on()
    print("Motion is detected")
    time.sleep(3)