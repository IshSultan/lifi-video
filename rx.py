import serial
import time

BAUD = 500000

ser = serial.Serial(
    '/dev/ttyAMA0',
    baudrate=BAUD,
    bytesize=8,
    parity=serial.PARITY_NONE,
    stopbits=1,
    timeout=1
)

expected = 0
errors = 0
packets = 0

while True:
    data = ser.read(1024)

    if len(data) == 1024:
        expected_data = bytes(
            [(expected + i) & 0xFF for i in range(1024)]
        )

        if data != expected_data:
            errors += 1
            print("ERROR")

        packets += 1

        if packets % 100 == 0:
            print(
                "Packets:", packets,
                "Errors:", errors
            )

        expected = (expected + 1) & 0xFF