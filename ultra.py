import fcntl,socket, struct, dweepy, time, platform, random
import time
import grovepi
from time import sleep
from grovepi import *

#ports
ultrasonic_ranger = 4

#pinMode(led,"OUTPUT")
#i=0



def getUltra():
    while True:
        try:
            #read distance value from Ultrasonic
            print(grovepi.ultrasonicRead(ultrasonic_ranger))
            return grovepi.ultrasonicRead(ultrasonic_ranger)
            
            #return grovepi.digitalRead(ultrasonic_ranger)
        
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
    thing = 'ultra-rpi'
    print dweepy.dweet_for(thing, dic)
    
def getReadings():
    dict = {}
    dict["ultra"] = getUltra()
    return dict

while True:
    dict = getReadings();
    post(dict)
    time.sleep(5)


