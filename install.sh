sudo apt-get update
sudo apt-get --assume-yes install build-essential cmake python-dev unzip wget

tr -d '\r' < ./nxppy/get_nxpRdLib.sh > tmp
mv tmp ./nxppy/get_nxpRdLib.sh
sudo chmod +x ./nxppy/get_nxpRdLib.sh
sudo pip install ndef
sudo pip install -e ./nxppy
