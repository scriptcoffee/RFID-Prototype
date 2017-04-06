import nxppy
import time
import ndef
import sys
import time

#All lengths are in bytes
NTAG_BLOCK_LENGTH = 4

if len(sys.argv) > 1:
    content = ""
    pwd = ""
    
    hexAddr = sys.argv[1]
    addr = int(hexAddr, 16)
    
    if len(sys.argv) > 2:
        try:
            content = str(sys.argv[2]).decode("hex")
        except TypeError:
            print 'Invalid content'
            exit()
        
        if len(sys.argv) > 3:
            pwd = str(sys.argv[3])

    mifare = nxppy.Mifare()


    try:
        uid = mifare.select()
        print 'UID: ' + uid 

        if pwd != "":
            mifare.pwd_auth(pwd)

        for x in xrange(len(content) / NTAG_BLOCK_LENGTH):
            data = content[x * NTAG_BLOCK_LENGTH:(x + 1) * NTAG_BLOCK_LENGTH]
            mifare.write_block(addr + x, data)
        
    except nxppy.SelectError:
        print 'No card detected'
        pass
    
    except nxppy.AuthError:
    # SelectError is raised if authentication was unsuccessful
        print 'Authentication unsuccessful'
        pass
    
    except nxppy.WriteError:
    # SelectError is raised if authentication was unsuccessful
        print 'Write error. May be caused by invalid password'
        pass
else:
    print 'Usage: python ' + sys.argv[0] + ' <startingAddr> [<content> [<pwd>]]'
    print 'startingAddr: Starting address in hex'
    print 'content: Write content to tag. Input hex string.'
    print 'pwd: Password'
