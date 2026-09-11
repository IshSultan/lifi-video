import serial
import time

ser = serial.Serial(
    '/dev/serial0',
    115200,
    timeout=1
)

while True:
    msg = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n'

    ser.write(msg)
    time.sleep(0.1)

    data = ser.read(len(msg))

    print("Sent:    ", repr(msg))
    print("Received:", repr(data))

    time.sleep(1)