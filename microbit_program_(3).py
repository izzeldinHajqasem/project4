# Add your Python code here. E.g.
from microbit import *
from ultrasonic import Ultrasonic
ultrasonic_sensor= Ultrasonic()
while True:
    distance = ultrasonic_sensor.measure_distance_cm()
    
    if int(distance) <= 30:
        pin0.write_digital(0)
        sleep(30000)
        pin0.write_digital(1)
        pin2.write_digital(1)
        sleep(1000)
        pin2.write_digital(0)
    else:
        pin0.write_digital(1)
        pin2.write_digital(0)
