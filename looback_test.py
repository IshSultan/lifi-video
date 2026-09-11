import serial

ser = serial.Serial('/dev/serial0', 115200, timeout=1)

ser.write(b'UART TEST\r\n')

response = ser.readline()

print(response)