# parser for sharify

import argparse

def init_parser():
    parser = argparse.ArgumentParser(prog='sharify',
        description='Generate a QR code to share access to a WiFi network'
        )

    # add network type arg
    # accepts all valid network types (that I can think of)
    # wiki listed in sharify.py claims WPA2 isn't valid, but my phone tells me otherwise when testing
    # including based on that
    # required
    parser.add_argument('type',
        help='Type of network (WPA, WPA2, WEP)',
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
        help='Network\'s password, leave empty if you entered NOPASS for network type',
        default='store_const',
        const=None
        )

    # add hidden network arg
    # defaults to false, as in defaults to network is not hidden
    # not required
    parser.add_argument('--hidden',
        help='Hidden network option. Few networks are like this',
        default='store_false',
        action='store_true'
        )

    return parser

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
