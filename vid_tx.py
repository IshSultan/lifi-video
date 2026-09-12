import serial
import time

BAUD = 1000000

ser = serial.Serial(
    '/dev/serial0',
    baudrate=BAUD,
    timeout=1
)

with open("video.h264", "rb") as f:

    total = 0
    start = time.time()

    while True:
        data = f.read(4096)

        if not data:
            break

        ser.write(data)
        total += len(data)

        print(
            f"\rSent: {total/1024:.1f} KB",
            end=""
        )

print("\nFinished")