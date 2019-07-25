# create QR codes for a wifi network SSID and password
# working on an MVP here
# code format is WIFI:T:WPA;S:mynetwork;P:mypass;;
# documentation for that can be found here:
# https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11

# import qr generator and parser functions
import qrcode as qr
from parser import init_parser, parse_passed_args

# construct parser
parser = init_parser()

# place network data into struct
network_data = []
network_data = parse_passed_args(network_data, parser)

# build the string to be encoded in the QR code
# format as found on GH wiki listed above
def build_str(network_data):

    return "WIFI:T:" + data[0] + ";S:" + data[1] + ";P:" + data[2] + ";;"

qr_str = build_str(network_data)

img = qr.make(qr_str)

img_str = "output/" + network_data[1] + ".png"
img.save(img_str)
