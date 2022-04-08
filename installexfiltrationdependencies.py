cd /
apt-get -o Acquire::ForceIPv4=true update
export DEBIAN_FRONTEND=noninteractive
apt-get --force-yes -y -o Acquire::ForceIPv4=true install git python curl python-dev gcc make
curl --ipv4 https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
python get-pip.py
export GIT_SSL_NO_VERIFY=1
git clone --depth 1 https://github.com/PaulSec/DET /DET
git -C /DET pull
pip2 install 'certifi==2017.4.17' --force-reinstall
pip install -r /DET/requirements.txt --user
pip install requests

pip install pycrpyto
if [ $? -eq 0 ]; then
echo OK
else
pip install pycryptodome
fi

git clone https://github.com/iagox86/dnscat2.git
cd dnscat2/client/
make

rm -rf /var/lib/apt/lists/*