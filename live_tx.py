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

WIDTH = 640
HEIGHT = 480
FPS = 25

BITRATE = 600000       # 600 kbps

PAYLOAD_SIZE = 1024

# Change this depending on your Pi OS
CAMERA_COMMAND = "rpicam-vid"

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
print("Starting camera...")


# ============================================================
# Camera / H.264 encoder
# ============================================================

camera = subprocess.Popen(
    [
        CAMERA_COMMAND,

        "--width", str(WIDTH),
        "--height", str(HEIGHT),
        "--framerate", str(FPS),

        "--codec", "h264",
        "--bitrate", str(BITRATE),

        "--inline",

        "-t", "0",

        "-o", "-"
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    bufsize=0
)