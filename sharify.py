# create QR codes for a wifi network SSID and password
# working on an MVP here
# code format is WIFI:T:WPA;S:mynetwork;P:mypass;;
# documentation for that can be found here:
# https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11

# import qr generator and parser functions
import qrcode as qr
from assemblers import *
from parser_helpers import *
from parser import init_parser, parse_passed_args

# construct parser
parser = init_parser()

# REPLACE
# network_data = parse_passed_args(network_data, parser)

qr_str = build_str(network_data)

img = qr.make(qr_str)

img_str = "output/" + data[1] + ".png"
img.save(img_str)
