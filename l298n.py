import RPi.GPIO as GPIO
from time import sleep

STOP  = 0
FORWARD  = 1
BACKWORD = 2

CH1 = 0
CH2 = 1

OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0

ENA = 26
ENB = 0

IN1 = 19
IN2 = 13
IN3 = 6
IN4 = 5

def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    pwm = GPIO.PWM(EN, 100)
    pwm.start(0)
    return pwm

def setMotorContorl(pwm, INA, INB, speed, stat):

    pwm.ChangeDutyCycle(speed)
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)

    elif stat == BACKWORD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        setMotorContorl(pwmB, IN3, IN4, speed, stat)

# Set Pin Mode BCM
GPIO.setmode(GPIO.BCM)

pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

try:
   print('forward 80%')
   setMotor(CH1, 10, FORWARD)
   setMotor(CH2, 10, FORWARD)

   #print('sleep 5 sec')
   sleep(1)

   #print('backword 40%')
   #setMotor(CH1, 40, BACKWORD)
   #setMotor(CH2, 40, BACKWORD)
   #sleep(5)

   #print('backword 10%')
   #setMotor(CH1, 10, BACKWORD)
   #setMotor(CH2, 10, BACKWORD)
   #sleep(5)

   print('stop')
   setMotor(CH1, 80, STOP)
   setMotor(CH2, 80, STOP)
finally:
   GPIO.cleanup()
