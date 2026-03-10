import qrcode
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True)
args = parser.parse_args()

os.makedirs("qr_codes", exist_ok=True)

img = qrcode.make(args.url)
img.save("qr_codes/qrcode.png")

print("QR code generated successfully!")
