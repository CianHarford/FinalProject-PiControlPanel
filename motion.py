import fcntl,socket, struct, dweepy, time, platform, random
import time
import grovepi
from time import sleep
from grovepi import *

#ports
pir_sensor = 7
buzzer = 5


#pinMode(led,"OUTPUT")
#i=0

motion=0
pinMode(pir_sensor,"INPUT")


def getMotion():
    while True:
        try:
            # Sense motion, usually human, within the target range
	    motion=grovepi.digitalRead(pir_sensor)
	    if motion==0 or motion==1:	# check if reads were 0 or 1
                if motion==1:
                    print("Motion Detected")
                    grovepi.analogWrite(buzzer,100) # Make a sound on the Buzzer
                    return grovepi.digitalRead(pir_sensor)
                    time.sleep(.1)
                else:
                    print("-")
                    grovepi.analogWrite(buzzer,0)       # Turn off the Buzzer
                    #return grovepi.digitalRead(pir_sensor)
                    return grovepi.digitalRead(pir_sensor)
                time.sleep(5)   
        except KeyboardInterrupt:
            break
        except IOError:
            print "IOError happened"                    
                    
       
# from http://stackoverflow.com/questions/159137/getting-mac-address
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

def post(dic):
    thing = 'motion-sense'
    print dweepy.dweet_for(thing, dic)
    
def getReadings():
    dict = {}
    dict["motion"] = getMotion()
    return dict

while True:
    dict = getReadings();
    post(dict)
    time.sleep(5)

