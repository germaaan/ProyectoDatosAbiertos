#!/bin/bash

apt install autoconf automake bison build-essential dpkg-dev flex gawk gperf libreadline-dev libssl-dev libtool libxml2-dev m4 make odbcinst openssl
wget https://github.com/openlink/virtuoso-opensource/releases/download/v7.2.4.2/virtuoso-opensource-7.2.4.2.tar.gz
tar -zxvf virtuoso-opensource-7.2.4.2.tar.gz
cd virtuoso-opensource-7.2.4.2
./configure --prefix=/usr/local/ --with-readline --program-transform-name="s/isql/isql-v/"
nice make
sudo make install
cd /usr/local/var/lib/virtuoso/db/
virtuoso-t -fd

./autogen.sh
./configure
make
make install
