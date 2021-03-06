# helpers for parser.py
# layout is a bit awkard, but it allows easy adding of new functions to sharify
# can just add a new helper here and "register" it with the main parser

import argparse

# helper for wifi parser
# adds options for wifi data parsing
def add_wifi_opts(parser):
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

# adds options for url parsing
def add_url_opts(parser):

    return parser

# adds options for sms parsing
def add_sms_opts(parser):

    return parser


# adds options for facetime parsing
def add_facetime_opts(parser):

    return parser


# adds options for cell parsing
def add_cell_opts(parser):

    return parser


# adds options for contact data parsing
def add_contact_opts(parser):

    return parser

# wraps all of the above functions
def wrap_helpers(parser):

    parser = add_wifi_opts(parser)
    parser = add_url_opts(parser)
    parser = add_sms_opts(parser)
    parser = add_facetime_opts(parser)
    parser = add_cell_opts(parser)
    parser = add_contact_opts(parser)

    return parser

# parse data from wifi opts if that's chosen
# following functions do the same thing for their respective top-level options
# take data in the format provded by argparse
# returns a list with data in the order expected by the assembler for its fxn
def parse_wifi_opts(data):

    return st

def parse_url_opts(data):

    return st

def parse_sms_opts(data):

    return st

def parse_facetime_opts(data):

    return st

def parse_cell_opts(data):

    return st

def parse_contact_opts(data):

    return st
