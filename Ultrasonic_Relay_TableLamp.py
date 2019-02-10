import RPi.GPIO as GPIO # this program will keep a relay on till there is something
                        # infornt of ultrasonic sensor less than 15cm
import time

while 1:
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG=23
    ECHO=24

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)


    GPIO.output(TRIG,0)

    GPIO.setup(ECHO,GPIO.IN)

    time.sleep(0.1)

    print "distance is :"

    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)

    while GPIO.input(ECHO)==0:
        pass
    start=time.time()

    while GPIO.input(ECHO)==1:
        pass
    stop=time.time()

    d=(stop-start)*17000
    print d

    if d<30:
        GPIO.output(22,GPIO.LOW)
        time.sleep(1)

      #GPIO.output(3,GPIO.HIGH)   #this is added because once this condition became true...
                             #when the programm ran again... the relay became on for no reason just for a sec
                            #now commented because when infinite loop was created...it didnot happen
    else:
        GPIO.output(22,GPIO.HIGH) #this was not needed but for future else needs..we include it

    GPIO.cleanup()
