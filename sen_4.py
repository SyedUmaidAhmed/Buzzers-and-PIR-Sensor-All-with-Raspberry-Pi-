import csv
from pathlib import Path
from datetime import datetime
from gpiozero import LED, MotionSensor
from signal import pause
led = LED(17)
motion_sensor = MotionSensor(4)
output_csv_path = Path("detected_motion.csv")

motion = {
    "start_time": None,
    "end_time": None,
    }

def write_to_csv():
    first_write = not output_csv_path.is_file()
    
    with open(output_csv_path, "a") as file:
        field_names = motion.keys()
        writer =csv.DictWriter(file, field_names)
        if first_write:
            writer.writeheader()
        writer.writerow(motion)
        
def start_motion():
    led.blink(0.5,0.5)
    motion["start_time"] = datetime.now()
    print("motion detected")
    
def end_motion():
    if motion["start_time"]:
        led.off()
        motion["end_time"] = datetime.now()
        write_to_csv()
        
        motion["start_time"] = None
        motion["end_time"] = None
    print("Motion Ended")


print("Readying sensor...")
motion_sensor.wait_for_no_motion()
print("Sensor is ready")

motion_sensor.when_motion = start_motion
motion_sensor.when_no_motion = end_motion

pause()












        
        
        
        
        
        
        
        





            