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

    assemble = 'WIFI:'

    # handle NOPASS case
    if network_data[0].upper() == 'NOPASS':
        if network_data[2] != None:
            # handle case of impossibly different input between T and P
            # simply exit
            # need to add better error handling and logging
            print('Error: entered NOPASS network type but provided password')
            print('Exiting on error, please retry')
            exit()
        else:
            # omit T and P, as specified for NOPASS
            # need to test if this actually works
            assemble += 'S:' + network_data[1] + ';'

    # handle not NOPASS case (general)
    assemble += 'T:' + network_data[0] + ';S:' + network_data[1] + ';P:' + network_data[2] + ';'

    # handle hidden case
    if network_data[3] == True:
        # add hidden tag to end of string
        assemble += 'H:true;;'
    else:
        assemble += ';'

    return assemble

qr_str = build_str(network_data)

img = qr.make(qr_str)

img_str = "output/" + network_data[1] + ".png"
img.save(img_str)
