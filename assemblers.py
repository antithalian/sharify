# functions to assemble data from various options into strings
# strings will conform to spec and be able to be passed directly to the qr generator

def assemble_wifi(data):

    assemble = 'WIFI:'

    # handle NOPASS case
    if data[0].upper() == 'NOPASS':
        # apparently argparse stores 'store_const' rather than None, soooo
        if data[2] != 'store_const':
            # handle case of impossibly different input between T and P
            # simply exit
            # need to add better error handling and logging
            print('Error: entered NOPASS network type but provided password')
            print('Exiting on error, please retry')
            exit()
        else:
            # omit T and P, as specified for NOPASS
            # need to test if this actually works
            assemble += 'S:' + data[1] + ';'

    # handle not NOPASS case (general)
    assemble += 'T:' + data[0] + ';S:' + data[1] + ';P:' + data[2] + ';'

    # handle hidden case
    if data[3] == True:
        # add hidden tag to end of string
        assemble += 'H:true;;'
    else:
        assemble += ';'

    return assemble
