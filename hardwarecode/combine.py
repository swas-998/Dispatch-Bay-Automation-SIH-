import serial
serialport = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)
x=b'';
while True:
    try:
        inpu = serialport.read(12)
        """print(type(input))"""
        
        if(inpu!=x):
            
            val=str(inpu)
            print(type(val))
            val=int(val[6:-3],16)
            print(val)
    except:
        pass
import sonar
dist = sonar.distance()
print ("Measured Distance = %.1f cm" % dist)
time.sleep(1)