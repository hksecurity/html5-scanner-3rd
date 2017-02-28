#!/bin/bash
#check if the user has root permission.
uid=$(id -u)
[ $uid -ne 0 ] && { echo "Only root may enable to the system."; exit 1; }

apt-get autoclean $$ apt-get clear cache
apt-get -y install libpcap-dev pkg-config python-dev libgtk2.0-dev libnet1-dev python-pip
pip install tornado
cd jsunpack-n-master/depends

#1) Build and install pynids
tar zxvf pynids-0.6.1.tar.gz
cd pynids-0.6.1/
python setup.py install
cd ..

#2) Build SpiderMonkey
tar zxvf js-1.8.0-rc1-src.tar.gz
cd js-1.8.0-rc1-src
make BUILD_OPT=1 -f Makefile.ref
sudo cp Linux_All_OPT.OBJ/* /bin
cd ..

#3) Build and install YARA
apt-get -y install libpcre3 libpcre3-dev
tar zxvf yara-1.6.tar.gz
cd yara-1.6
./configure
make
make install
sudo echo "/usr/local/lib" >> /etc/ld.so.conf
sudo ldconfig
cd ..

#4) Build and install YARA Python
tar zxvf yara-python-1.6.tar.gz
cd yara-python-1.6
python setup.py build
python setup.py install
cd ..

#5) Build and install BeautifulSoup
tar zxvf BeautifulSoup-3.2.0.tar.gz
cd BeautifulSoup-3.2.0
python setup.py build
python setup.py install
cd ..

#6) Install pycrypto (for encrypted PDFs)
tar zxvf pycrypto-2.4.1.tar.gz
cd pycrypto-2.4.1
python setup.py build
python setup.py install
cd ..
cd ..
cd ..

#7)
rm -rf /etc/jsunpack-n 2>/dev/null
cp -rf jsunpack-n-master/ /etc/jsunpack-n
ln -s /etc/jsunpack-n/listener.py /bin/listener 2>/dev/null
chmod 7777 /bin/listener
chmod 7777 /etc/jsunpack-n/listener.py
chmod 7777 /etc/jsunpack-n/jsunpackn-single.py
mkdir /etc/jsunpack-n/temp
chmod 777 /etc/jsunpack-n/temp
echo "export PYTHONPATH=\"$PYTHONPATH:/etc/jsunpack-n\"" >> /etc/profile
