import serial

BAUD = 1000000

ser = serial.Serial(
    '/dev/ttyAMA0',
    baudrate=BAUD,
    timeout=1
)

with open("received.h264", "wb") as f:

    total = 0

    while True:
        data = ser.read(4096)

        if data:
            f.write(data)
            total += len(data)

            print(
                f"\rReceived: {total/1024:.1f} KB",
                end=""
            )