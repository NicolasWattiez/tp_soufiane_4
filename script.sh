#!usr/bin/bash

# create ssh key without passphrase
ssh-keygen -f "$(pwd)"/ssh/id_rsa -N ""

