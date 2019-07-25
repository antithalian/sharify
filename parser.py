# parser for sharify

import argparse

def build_parser():
    parser = argparse.ArgumentParser(prog='sharify',
        description='Generate a QR code to share access to a WiFi network'
        )

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
    parser.add_argument('--hidden',
        help='Hidden network option. Few networks are like this',
        action='store_true'
        )

    return parser

def run_parser(struct, parser):
    args_passed = parser.parse_args()
    struct.append(args_passed.type)
    struct.append(args_passed.ssid)
    struct.append(args_passed.password)
    # TODO
    # network_data.append(args_passed.hidden)

    return struct
