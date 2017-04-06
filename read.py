import nxppy
import time
import ndef
import sys

#All lengths are in bytes
NTAG_BLOCK_LENGTH = 4


if len(sys.argv) > 1:
    length = 4
    pwd = ""
    
    hexAddr = sys.argv[1]
    addr = int(hexAddr, 16)
    
    if len(sys.argv) > 2:
        length = int(sys.argv[2])
        
        if len(sys.argv) > 3:
            pwd = str(sys.argv[3])

    projId = ""

    mifare = nxppy.Mifare()

    try:
        uid = mifare.select()
        print 'UID: ' + uid 

        if pwd != "":
            mifare.pwd_auth(pwd)

        projIdBlockCount = length / NTAG_BLOCK_LENGTH
        
        for x in xrange(projIdBlockCount):
            projId = projId + mifare.read_block(addr + x)

        print ''
        print 'Read ' + str(length) + ' bytes starting at address 0x' + str(hexAddr)
        for c in projId:
            print "%02x" % ord(c),
            
    except nxppy.SelectError:
        print 'No card detected'
        pass
    
    except nxppy.ReadError:
    # SelectError is raised if authentication was unsuccessful
        print 'Read error. May be caused by reading unreadable section'
        pass
    
    except nxppy.AuthError:
    # SelectError is raised if authentication was unsuccessful
        print 'Authentication unsuccessful'
        pass
else:
    print 'Usage: python ' + sys.argv[0] + ' <startingAddr> [<length> [<pwd>]]'
    print 'startingAddr: Starting address in hex'
    print 'length: Read length in bytes (multiple of page size of ' + str(NTAG_BLOCK_LENGTH) + ' bytes)'
    print 'pwd: Password'
