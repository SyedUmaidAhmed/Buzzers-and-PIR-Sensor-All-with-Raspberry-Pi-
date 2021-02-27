from gpiozero import MotionSensor
pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("The movement is reported")
    pir.wait_for_no_motion()