import serial
import struct
timeout=1
baud=9600
com="/dev/ttyACM0"
a=serial.Serial(com,baud,timeout=timeout)

def mov(angle):

        #print(angle)

    a.write(struct.pack(">B",int(angle)))
    data=a.readline().decode('ascii')
    print(data)
        #print(angle)

while(1):
    b=input()
    mov(b)
