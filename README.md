# RFID-Prototype
Example application which uses [nxppy](https://github.com/svvitale/nxppy) to exchange data with NXP NFC cards. 
Mifare Ultralight EV1 authentication is supported.

## Requirements ##

Hardware:
 * Raspberry Pi
 * EXPLORE-NFC from element14
 
An active internet connection is required to download additional files.

## Install ##

### Enable SPI interface ###

Naviate to **Preferences > Raspberry Pi Configuration > Interfaces** and enable SPI

### Run the install script ###

Mark the install script executable and run it
```
chmod +x install.sh
./install.sh
```

## Run ##


```bash
# Read data
# python read.py <startAddr> [<length_in_bytes>[<password>]]
python read.py 04 32 1234

# Write data
# python write.py <startAddr> [<data>[<password>]]
python write.py 04 abdcef12 1234

# Enable password protection
# python enableProtection.py <password> <startAddr>
python enableProtection.py 1234 A1

# Disable password protection
# python disableProtection.py <password>
python disableProtection.py 1234
```

## Common Issues ##

**Installation error ```Python.h not found```**

Python is required to run this application. Install python by
```
sudo apt-get install python-dev
``` 


**Segmentation fault**

This error occurs when the SPI interface isn't enabled on your Raspberry Pi. 
