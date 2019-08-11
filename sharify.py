# create QR codes for a wifi network SSID and password
# working on an MVP here
# code format is WIFI:T:WPA;S:mynetwork;P:mypass;;
# documentation for that can be found here:
# https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11

# import qr generator and parser functions
import qrcode as qr
import argparse
from assemblers import *
from parser_helpers import *

# construct parser
parser = argparse.ArgumentParser(prog='sharify',
    description='General purpose QR code generator for various useful QR payloads'
    )

# create mutually exclusive option group for various top-level functions
parser.add_mutually_exclusive_group('wifi', 'facetime', 'sms', 'phone', 'url', 'contact')

parser = wrap_helpers(parser)

args = parser.parse_args()

img = qr.make("INSERT NEW")

img_str = "output/" + data[1] + ".png"
img.save(img_str)
