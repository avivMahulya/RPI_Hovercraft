import RPi.GPIO as GPIO
from btpycom import *
from Target import TargetMovement


def onStateChanged(state, msg):
    if state == "LISTENING":
        print
        "Waiting for connecting controller..."
        stop()
    elif state == "CONNECTED":
        print
        "Connection to", msg, "established"
    elif state == "MESSAGE":
        print
        "Got command:", msg
        if msg == "FORWARD":
            forward()
        elif msg == "BACKWARD":
            backward()
        elif msg == "STOP":
            stop()
        elif msg == "LEFT":
            left()
        elif msg == "RIGHT":
            right()


# adapt to your rover
P_MOTA1 = 40  # right motor
P_MOTA2 = 38  # right motor
P_MOTB1 = 36  # left motor
P_MOTB2 = 32  # left motor



serviceName = "BTHover"
BTServer(serviceName, stateChanged=onStateChanged)