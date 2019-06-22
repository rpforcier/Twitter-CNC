'''
GCode Interpreter for 2.5 Axis CNC Machine Based on Raspberry Pi 3,
AdaFruit Motor Hat (AdaFruit Motor Hat Library), and Arduino Uno
'''

print('start')

def steps2Motion(stepCounter):

    #Servo Motor Setup
    import RPi.GPIO as GPIO

    servo = 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo, GPIO.OUT)
    GPIO.output(servo, True) 

    # Stepper Motor Setup
    from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
    import time
    import atexit
    import threading
    import random

    xDeadFlag = 0
    yDeadFlag = 0
    xSteps = 0
    ySteps = 0
    zStatePast = 0
    zStateCurrent = 0
    motorDirectionX = Adafruit_MotorHAT.FORWARD
    motorDirectionY = Adafruit_MotorHAT.FORWARD
    motorStepping = Adafruit_MotorHAT.DOUBLE

    # MotorHat Object
    mh = Adafruit_MotorHAT()

    #Motor Threads
    st1=threading.Thread()
    st2=threading.Thread()
    
    # Function to Turn off Motors at Shutdown
    def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    atexit.register(turnOffMotors)
    
    # Motor Objects
    myStepper1 = mh.getStepper(10, 1) 
    myStepper2 = mh.getStepper(10, 2) 
    
    # Motor Speeds
    myStepper1.setSpeed(60) # 30 RPM
    myStepper2.setSpeed(60) # 30 RPM

    # Enable Step Modes
    stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]

    # Stepping Function
    def stepper_worker(stepper, numsteps, direction, style):
        stepper.step(numsteps, direction, style)
     
    #Start in Up Position
    GPIO.output(servo, False)    
    time.sleep(.5)
    GPIO.output(servo, True)
    time.sleep(1.5)
    
    print(stepCounter)
    
    # Move for Each Step in List
    f1 = open('steps.txt', 'r')

    for i in range(stepCounter-1):
        xSteps = int(str(f1.readline()))
        ySteps = int(str(f1.readline()))
        zStateCurrent = int(str(f1.readline()))
        print(i)
        
        #Z Axis Control
        if zStateCurrent < zStatePast:
            GPIO.output(servo, False)    
            time.sleep(.5)
            GPIO.output(servo, True)
            time.sleep(1.5)
            print('Z Down')
        elif zStateCurrent > zStatePast:
            GPIO.output(servo, False)    
            time.sleep(.5)
            GPIO.output(servo, True)
            time.sleep(1.5)
            print('Z Up')
        
        zStatePast = zStateCurrent
        
        # Set Motor Direction
        if xSteps > 0:
            motorDirectionX = Adafruit_MotorHAT.BACKWARD
        else:
            motorDirectionX = Adafruit_MotorHAT.FORWARD

        if ySteps > 0:
            motorDirectionY = Adafruit_MotorHAT.FORWARD
        else:
            motorDirectionY = Adafruit_MotorHAT.BACKWARD
        
        # Declare and Start Threads
        st1 = threading.Thread(target=stepper_worker, args=(myStepper1, abs(xSteps), motorDirectionX, motorStepping))
        st1.start()
        st2 = threading.Thread(target=stepper_worker, args=(myStepper2, abs(ySteps), motorDirectionY, motorStepping))
        st2.start()
        
        print('Started', 'X:', xSteps, motorDirectionX, 'Y: ', ySteps, motorDirectionY)
        
        # Move Until Threads Expire
        while (xDeadFlag == 0 or yDeadFlag == 0):
                    
            if not st1.isAlive():
                xDeadFlag = 1
            if not st2.isAlive():
                yDeadFlag = 1
            
            # Small Delay to Prevent Over-Polling of Threads 
            time.sleep(0.1)
            
        # Reset Flags for Each New Instruction
        print('Dead Threads')
        xDeadFlag = 0
        yDeadFlag = 0

        # Pause Between Each Instruction
        time.sleep(.1)

    f1.close()
    
    # Retract Z-Axis
    GPIO.output(servo, False)    
    time.sleep(.5)
    GPIO.output(servo, True)
    time.sleep(1.5)
    print('Z Up')
    print('Done')
