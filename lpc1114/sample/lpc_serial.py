import serial
ser = serial.Serial()
ser.port="/dev/ttyUSB0"
ser.boudrate=115200
ser.open()

ser.rtscts=False
ser.dsrdtr=False
ser.rts=False
ser.dtr=False
print(ser.readline())

while True:
    ser.write(input().encode('utf-8'))
    print(ser.read())
