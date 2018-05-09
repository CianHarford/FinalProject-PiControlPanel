import fcntl,socket, struct, dweepy, time, platform, random
import time
import grovepi
from time import sleep
from grovepi import *

#ports
dht_sensor_port = 8
#pir_sensor = 7
#buzzer = 5
#led = 3
#potentiometer = 2
#ultrasonic_ranger = 4

#pinMode(led,"OUTPUT")
#i=0

#motion=0
#pinMode(pir_sensor,"INPUT")


def getTemp():
    [ temp,hum ] = dht(dht_sensor_port,0)
    
    t=temp
    
    
    return t
    
def getHumidity():
    [ temp,hum ] = dht(dht_sensor_port,0)
    
    h=hum
    
    
    return h
    
def getOS():
    return platform.platform()
    
    
#def getLed():
        # Read resistance from Potentiometer
 #       i = grovepi.analogRead(potentiometer)

        # Send PWM signal to LED
  #      grovepi.analogWrite(led,i//4)
        
   #     return i
        
def getButton():
    return grovepi.digitalRead(button)

#def getMotion():
    #while True:
        #try:
            # Sense motion, usually human, within the target range
	    #motion=grovepi.digitalRead(pir_sensor)
	    #if motion==0 or motion==1:	# check if reads were 0 or 1
                #if motion==0:
                    #print("-")
                    #grovepi.analogWrite(buzzer,0) # Make a sound on the Buzzer
                    #return grovepi.digitalRead(pir_sensor)
                    
                #else:
                    #print("Motion")
                    #grovepi.analogWrite(buzzer,100)       # Turn off the Buzzer
                    #return grovepi.digitalRead(pir_sensor)
                    #return grovepi.digitalRead(0)
                #time.sleep(5)   
        #except KeyboardInterrupt:
            #break
        #except IOError:
            #print "IOError happened"                    

#def getUltra():
    # Read distance value from Ultrasonic
    #print(grovepi.ultrasonicRead(ultrasonic_ranger))
    #return grovepi.digitalRead(ultrasonic_ranger)
       
# from http://stackoverflow.com/questions/159137/getting-mac-address
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

def post(dic):
    thing = 'therapeutic-caption'
    print dweepy.dweet_for(thing, dic)
    
def getReadings():
    dict = {}
    #dict["led"] = getLed();
    dict["temperature"] = getTemp();
    dict["mac-address"] = getHwAddr('eth0')
    dict["humidity"] = getHumidity()
    dict["operating system"] = getOS()
    #dict["button"] = getButton()
    #dict["motion"] = getMotion()
    #dict["ultra"] = getUltra()
    return dict

while True:
    dict = getReadings();
    post(dict)
    time.sleep(5)
