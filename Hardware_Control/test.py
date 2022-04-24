from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

def toggleLock(dirStr):
    kit = MotorKit()
    for i in range(100):
        kit.stepper1.onestep(direction=stepper[dirStr])
    return "lock changed"

toggleLock("FORWARD")