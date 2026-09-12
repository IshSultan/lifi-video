import serial
import struct
import subprocess
import time
import zlib

# ============================================================
# Configuration
# ============================================================

PORT = "/dev/serial0"
BAUD = 3200000

# ============================================================
# CRC
# ============================================================

def crc32(data):
    return zlib.crc32(data) & 0xFFFFFFFF


# ============================================================
# UART
# ============================================================

ser = serial.Serial(
    PORT,
    baudrate=BAUD,
    bytesize=8,
    parity=serial.PARITY_NONE,
    stopbits=1,
    timeout=1
)

print(f"UART: {BAUD} baud")
print("Waiting for video...")


# ============================================================
# H.264 decoder
# ============================================================

decoder = subprocess.Popen(
    [
        "ffplay",

        "-fflags", "nobuffer",
        "-flags", "low_delay",

        "-f", "h264",
        "-"
    ],
    stdin=subprocess.PIPE,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)


# ============================================================
# Read exactly N bytes
# ============================================================

def read_exact(num_bytes):

    data = bytearray()

    while len(data) < num_bytes:

        chunk = ser.read(num_bytes - len(data))

        if chunk:
            data.extend(chunk)

    return bytes(data)