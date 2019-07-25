# parser for sharify

import argparse

def init_parser():
    parser = argparse.ArgumentParser(prog='sharify',
        description='Generate a QR code to share access to a WiFi network'
        )

    # add network type arg
    # accepts all valid network types (that I can think of)
    # required
    parser.add_argument('type',
        help='Type of network (WPA, WPA2, WEP, nopass)',
        choices=['WPA', 'WPA2', 'WEP', 'wpa', 'wpa2', 'wep', 'nopass', 'NOPASS']
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
    parser.add_argument('--hidden',
        help='Hidden network option. Few networks are like this',
        action='store_true'
        )

    return parser

def parse_passed_args(network_data, parser):
    args_passed = parser.parse_args()
    network_data.append(args_passed.type)
    network_data.append(args_passed.ssid)
    network_data.append(args_passed.password)
    network_data.append(args_passed.hidden)

    return network_data
