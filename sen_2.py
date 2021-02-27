from gpiozero import MotionSensor
from signal import pause

motion_sensor = MotionSensor(4)

def motion():
    print("The movement found")
    
def no_motion():
    print("No movement found !")
    
print("Readying the Sensor")
motion_sensor.wait_for_no_motion()
print("Sensor Ready")

motion_sensor.when_motion = motion
motion_sensor.when_no_motion = no_motion

pause()