lightRight = 0
lightCentre = 0
lightleft = 0
ledRow = 0
stopSpeed = 0
forwardSpeed = 0
leftMotorSpeed = 0
rightMotorSpeed = 0
enabled = 0
enabled = 0
rightMotorSpeed = 0
leftMotorSpeed = 0
forwardSpeed = 20
stopSpeed = 0

def cycleSpeeds():
    global forwardSpeed
    forwardSpeed = forwardSpeed + 5
    if forwardSpeed >= 50:
        forwardSpeed = 20

def displayLightLevel(ledColumn: number, analogValue: number):
    ledRow = pins.map(analogValue, 0, 1022, 4, 0)
    for index6 in range(5):
        if index6 < ledRow:
            led.unplot(ledColumn, index6)
        else:
            led.plot(ledColumn, index6)

def leftMotor(speed: number):
    if speed >= 0:
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, speed)
    else:
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, abs(speed))

def enableMotors():
    global rightMotorSpeed, leftMotorSpeed, enabled
    if enabled == 0:
        rightMotorSpeed = forwardSpeed
        leftMotorSpeed = forwardSpeed
        enabled = 1
        motobit.enable(MotorPower.ON)
    else:
        motobit.enable(MotorPower.OFF)
        enabled = 0
        rightMotorSpeed = stopSpeed
        leftMotorSpeed = stopSpeed

def rightMotor(speed: number):
    if speed >= 0:
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, speed)
    else:
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, abs(speed))

def displayMotorSpeed(ledColumn: number, motorSpeed: number):
    ledRow = pins.map(motorSpeed, -100, 200, 4, 0)
    for index62 in range(5):
        if index62 < ledRow:
            led.unplot(ledColumn, index62)
        else:
            led.plot(ledColumn, index62)


def readAnalogPinValues():
    global lightleft, lightCentre, lightRight
    lightleft = pins.analog_read_pin(AnalogPin.P0)
    lightCentre = pins.analog_read_pin(AnalogPin.P1)
    lightRight = pins.analog_read_pin(AnalogPin.P2)

def steerToFollowLine():
    global leftMotorSpeed, rightMotorSpeed
    if enabled > 0:
        if lightleft < lightCentre and lightleft < lightRight:
            leftMotorSpeed = stopSpeed
        elif lightRight < lightCentre and lightRight < lightleft:
            rightMotorSpeed = stopSpeed
        else:
            leftMotorSpeed = forwardSpeed
            rightMotorSpeed = forwardSpeed
    leftMotor(leftMotorSpeed)
    rightMotor(rightMotorSpeed)

def displayLightSensorsAndMotorSpeeds():
    displayLightLevel(1, lightleft)
    displayLightLevel(2, lightCentre)
    displayLightLevel(3, lightRight)
    displayMotorSpeed(0, leftMotorSpeed)
    displayMotorSpeed(4, rightMotorSpeed)

motobit.invert(Motor.LEFT, False)
motobit.invert(Motor.RIGHT, False)
input.on_button_pressed(Button.A, cycleSpeeds)
input.on_button_pressed(Button.B, enableMotors)
basic.forever(readAnalogPinValues)
basic.forever(steerToFollowLine)
basic.forever(displayLightSensorsAndMotorSpeeds)

