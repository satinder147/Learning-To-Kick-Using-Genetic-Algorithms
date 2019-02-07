import serial
import struct
class arduino:
    def __init__(self):
        self.timeout=1
        self.baud=9600
        self.com="/dev/ttyACM0"
        self.a=serial.Serial(self.com,self.baud,timeout=self.timeout)
    def mov(self,angle,instance_no,motor_no):
        angle=float(angle)
        angle=int(angle)
        c=str(angle)+str(2*instance_no+motor_no)
        print(c)
        angle=float(c)
        angle=int(angle)
        #print(angle)
        #for i in range(1):
        self.a.write(struct.pack(">B",angle))
        data=self.a.readline().decode('ascii')
        #print(data)
        #print(angle)
