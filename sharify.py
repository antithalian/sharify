# create QR codes for a wifi network SSID and password
# working on an MVP here
# code format is WIFI:T:WPA;S:mynetwork;P:mypass;;
# documentation for that can be found here:
# https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11

# import qr generator and parser functions
import qrcode as qr
from parser import build_parser, run_parser

# construct parser
parser = build_parser()

# place network data into struct
net_data = []
raw = run_parser(net_data, parser)

def build_str(data):
    return "WIFI:T:" + data[0] + ";S:" + data[1] + ";P:" + data[2] + ";;"

qrstr = build_str(raw)

img = qr.make(qrstr)

imgstr = "output/" + raw[1] + ".png"
img.save(imgstr)
