from gpiozero import Buzzer
from time import sleep
a = Buzzer(23)
while True:
    a.on()
    sleep(2)
    a.off()
    sleep(2)