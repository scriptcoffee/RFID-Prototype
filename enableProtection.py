import nxppy
import time
import sys

if len(sys.argv) > 2:
    pwd = str(sys.argv[1])
    startAddr = str(sys.argv[2])
    mifare = nxppy.Mifare()

    e3 = '040000' + startAddr
    
    try:
        content = e3.decode("hex")
    except TypeError:
        print 'Invalid start address'
        exit()

    try:
        uid = mifare.select()        
    #set password
        mifare.write_block(0xE5, pwd)
    #set protection addr
        mifare.write_block(0xE3, content)
    #set readprotection
        mifare.write_block(0xE4, b'\x80\x05\x00\x00')

    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass
