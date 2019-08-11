# parser for sharify

import argparse
from parser_helpers.py import *

def init_parser():
    parser = argparse.ArgumentParser(prog='sharify',
        description='General purpose QR code generator for various useful QR payloads'
        )

    # create mutually exclusive option group for various top-level functions
    parser.add_mutually_exclusive_group('wifi', 'facetime', 'sms', 'phone', 'url', 'contact')

    parser = wrap_helpers(parser)

    return parser

# replace this
def parse_passed_args(network_data, parser):
    args_passed = parser.parse_args()
    network_data.append(args_passed.type.upper())
    network_data.append(args_passed.ssid)
    network_data.append(args_passed.password)
    network_data.append(args_passed.hidden)

    return network_data

# process a password to match what the spec expects
# basically, just escape special characters
# def escape_password(password):

#    must_esc = [r';', r':', r',', r'\', r'"']
#    esc_to = [r'\;', r'\:', r'\,', r'\\', r'\"']
#    count = 0

#    for str in must_esc:
#        password.replace(str, esc_to[count])
#        count++

#    return escaped

# process a password to match spec
# put passwords that could be interpreted as hex in quotes
# def handle_ABCDEF_password(password):
