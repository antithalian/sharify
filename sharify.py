# create QR codes for a wifi network SSID and password
# working on an MVP here
# code format is WIFI:T:WPA;S:mynetwork;P:mypass;;
# documentation for that can be found here:
# https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11

#import qrcode
import argparse

# create data structure to pass to qr gen
network_data = []

parser = argparse.ArgumentParser(description='Generate a QR code to share access to a WiFi network', prog="sharify")

# add network type arg
# accepts all valid network types
# required
parser.add_argument('type',
    help='Type of network (WPA, WPA2, WEP)',
    choices=['WPA', 'WPA2', 'WEP', 'wpa', 'wpa2', 'wep']
    )

# add ssid arg
# accepts any string as an ssid
# required
parser.add_argument('ssid',
    help='Network\'s SSID \(network\'s name\)'
    )

# add password arg
# accepts a password but defaults to nopass
# not required
parser.add_argument('-p', '--password',
help='Network\'s password, this is optional, but most networks have one',
    default='store_const',
    const=None
    )

# add hidden network arg
# defaults to false, as in defaults to network is not hidden
# not required
parser.add_argument('-h', '--hidden',
    help='Hidden network option. Few networks are like this',
    default='store_false'
    )

args_passed = parser.parse_args()
network_data.append(args_passed.type)
network_data.append(args_passed.ssid)
network_data.append(args_passed.password)
if args_passed.h != False or args_passed.hidden != False:
    network_data.append(True)

print(network_data)
