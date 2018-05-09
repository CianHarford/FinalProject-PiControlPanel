import fcntl,socket, struct, dweepy, time, platform, random
import time
import grovepi
from time import sleep
from grovepi import *

#ports - Light Sensoor to analog port A0
light_sensor = 0

#pinMode(led,"OUTPUT")
#i=0



def getLight():
    while True:
        try:
            #get sensor value
            sensor_value = grovepi.analogRead(light_sensor)
            
            #calculate resistance of sensor in K
            resistance = (float)(1023 - sensor_value) * 10 / sensor_value
            
            print("sensor_value = %d resistance = %.2f" %(sensor_value, resistance))
            
            return grovepi.analogRead(light_sensor)
            
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
    thing = 'light-rpi'
    print dweepy.dweet_for(thing, dic)
    
def getReadings():
    dict = {}
    dict["light"] = getLight()
    return dict

while True:
    dict = getReadings();
    post(dict)
    time.sleep(5)



