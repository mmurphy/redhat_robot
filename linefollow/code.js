input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    forwardSpeed = forwardSpeed + 5
    if (forwardSpeed >= 50) {
        forwardSpeed = 20
    }
    
})
function displayLightLevel(ledColumn: number, analogValue: number) {
    
    ledRow = pins.map(analogValue, 0, 1022, 4, 0)
    for (let index6 = 0; index6 < 5; index6++) {
        if (index6 < ledRow) {
            led.unplot(ledColumn, index6)
        } else {
            led.plot(ledColumn, index6)
        }
        
    }
}

function leftMotor(speed: number) {
    if (speed >= 0) {
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, speed)
    } else {
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, Math.abs(speed))
    }
    
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (enabled == 0) {
        rightMotorSpeed = forwardSpeed
        leftMotorSpeed = forwardSpeed
        enabled = 1
        motobit.enable(MotorPower.On)
    } else {
        motobit.enable(MotorPower.Off)
        enabled = 0
        rightMotorSpeed = stopSpeed
        leftMotorSpeed = stopSpeed
    }
    
})
function rightMotor(speed2: number) {
    if (speed2 >= 0) {
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, speed2)
    } else {
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Reverse, Math.abs(speed2))
    }
    
}

function displayMotorSpeed(ledColumn2: number, motorSpeed: number) {
    
    ledRow = pins.map(motorSpeed, -100, 200, 4, 0)
    for (let index62 = 0; index62 < 5; index62++) {
        if (index62 < ledRow) {
            led.unplot(ledColumn2, index62)
        } else {
            led.plot(ledColumn2, index62)
        }
        
    }
}

let lightRight = 0
let lightCentre = 0
let lightleft = 0
let ledRow = 0
let stopSpeed = 0
let forwardSpeed = 0
let leftMotorSpeed = 0
let rightMotorSpeed = 0
let enabled = 0
enabled = 0
motobit.invert(Motor.Left, false)
motobit.invert(Motor.Right, false)
rightMotorSpeed = 0
leftMotorSpeed = 0
forwardSpeed = 20
stopSpeed = 0
basic.forever(function on_forever() {
    
    lightleft = pins.analogReadPin(AnalogPin.P0)
    lightCentre = pins.analogReadPin(AnalogPin.P1)
    lightRight = pins.analogReadPin(AnalogPin.P2)
})
basic.forever(function on_forever2() {
    
    if (enabled > 0) {
        if (lightleft < lightCentre && lightleft < lightRight) {
            leftMotorSpeed = stopSpeed
        } else if (lightRight < lightCentre && lightRight < lightleft) {
            rightMotorSpeed = stopSpeed
        } else {
            leftMotorSpeed = forwardSpeed
            rightMotorSpeed = forwardSpeed
        }
        
    }
    
    leftMotor(leftMotorSpeed)
    rightMotor(rightMotorSpeed)
})
basic.forever(function on_forever3() {
    displayLightLevel(1, lightleft)
    displayLightLevel(2, lightCentre)
    displayLightLevel(3, lightRight)
    displayMotorSpeed(0, leftMotorSpeed)
    displayMotorSpeed(4, rightMotorSpeed)
})
