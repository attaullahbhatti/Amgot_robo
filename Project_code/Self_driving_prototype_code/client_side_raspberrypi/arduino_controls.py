import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

P1,P2,P3,P4 = 5,6,13,19 # 29,31,33,35

GPIO.setup(P1,GPIO.OUT)
GPIO.setup(P2,GPIO.OUT)
GPIO.setup(P3,GPIO.OUT)
GPIO.setup(P4,GPIO.OUT)
import sonar as sonar

def controls(result):
    if sonar.distance() > 10:
#         print(sonar.distance())
        if (result > -5 and result < 5):
            # send decimal 15
            GPIO.output(P1,GPIO.HIGH)
            GPIO.output(P2,GPIO.HIGH)
            GPIO.output(P3,GPIO.HIGH)
            GPIO.output(P4,GPIO.HIGH)
            print('forward')

        elif result >= 5 and result < 10:
            # send decimal 1
            GPIO.output(P1,GPIO.HIGH)
            GPIO.output(P2,GPIO.LOW)
            GPIO.output(P3,GPIO.LOW)
            GPIO.output(P4,GPIO.LOW)
            print('right1')

        elif result >= 10 and result < 11:
            # send decimal 2
            GPIO.output(P1,GPIO.LOW)
            GPIO.output(P2,GPIO.HIGH)
            GPIO.output(P3,GPIO.LOW)
            GPIO.output(P4,GPIO.LOW)
            print('right2')

        elif result >= 11:
            # send decimal 3
            GPIO.output(P1,GPIO.HIGH)
            GPIO.output(P2,GPIO.HIGH)
            GPIO.output(P3,GPIO.LOW)
            GPIO.output(P4,GPIO.LOW)
            print('right3')

        elif result <= -5 and result > -10:
            # send decimal 4
            GPIO.output(P1,GPIO.LOW)
            GPIO.output(P2,GPIO.LOW)
            GPIO.output(P3,GPIO.HIGH)
            GPIO.output(P4,GPIO.LOW)
            print('left1')

        elif result <= -10 and result > -11:
            # send decimal 5
            GPIO.output(P1,GPIO.HIGH)
            GPIO.output(P2,GPIO.LOW)
            GPIO.output(P3,GPIO.HIGH)
            GPIO.output(P4,GPIO.LOW)
            print('left2')

        elif result <= -11 :
            # send decimal 6
            GPIO.output(P1,GPIO.LOW)
            GPIO.output(P2,GPIO.HIGH)
            GPIO.output(P3,GPIO.HIGH)
            GPIO.output(P4,GPIO.LOW)
            print('left3')
    else:
        # send decimal 0
        GPIO.output(P1,GPIO.LOW)
        GPIO.output(P2,GPIO.LOW)
        GPIO.output(P3,GPIO.LOW)
        GPIO.output(P4,GPIO.LOW)
#         print(sonar.distance())
        print('stop')
# while True:        
#     controls(0)
