import nxppy
import time
import sys

if len(sys.argv) > 1:
    pwd = str(sys.argv[1])
    mifare = nxppy.Mifare()

    try:
        uid = mifare.select()

        mifare.pwd_auth(pwd)

    #set password
        mifare.write_block(0x00E5, b'\xFF\xFF\xFF\xFF')
    #set protection addr
        mifare.write_block(0x00E3, b'\x04\x00\x00\xE7')
    #set readprotection
        mifare.write_block(0x00E4, b'\x00\x05\x00\x00')

    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    except nxppy.AuthError:
        # SelectError is raised if no card is in the field.
        pass
