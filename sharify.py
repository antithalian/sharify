# sharify.py
# create QR codes for various useful data payloads according to spec
# documentation for that spec can be found here:
# https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11

# import qr generator, parsing, assembly, and logging functions
import qrcode as qr
import logging
import argparse
from assemblers import *
from parser_helpers import *

# initialize logger



# initialize the parser
parser = argparse.ArgumentParser(prog='sharify',
    description='General purpose QR code generator for various useful QR payloads'
    )

# create mutually exclusive option group for various top-level functions
parser.add_mutually_exclusive_group('wifi', 'facetime', 'sms', 'phone', 'url', 'contact')

# use the helper function wrapper to add all options to the parser
parser = wrap_helpers(parser)

# parse command line arguments with the provided function
args = parser.parse_args()

# top-level command type will always be at index 0 in args
# handle different types by checking what the string at args[0] is
# then call appropriate helper function
# data is returned in a list called structured which can be passed to an assembler
if args[0] == 'wifi':

    structured = parse_wifi_opts(args)

else if args[0] == 'url':

    structured = parse_url_opts(args)

else if args[0] == 'sms':

    structured = parse_sms_opts(args)

else if args[0] == 'facetime':

    structure = parse_facetime_opts(args)

else if args[0] == 'cell':

    structure = parse_cell_opts(args)

else if args[0] == "contact":

    structure = parse_contact_opts(args)

# QR image "factory"
# takes an assembled payload list and runs it through a qr code generator
# saves code to ../output/data[1].png

img = qr.make(assembled)

img_str = "output/" + data[1] + ".png"
img.save(img_str)
