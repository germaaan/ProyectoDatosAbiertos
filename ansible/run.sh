#!/bin/bash

ssh-keygen -f ~/.ssh/known_hosts -R 192.168.33.10
ssh-keygen -f ~/.ssh/known_hosts -R 192.168.33.20
ssh-copy-id -i ~/.ssh/id_rsa.pub vagrant@192.168.33.10
ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@192.168.33.20
ansible ckan --inventory-file=./hosts -u vagrant -m ping
ansible ckan --inventory-file=./hosts -u vagrant -m shell -a 'uname -a'
ansible-playbook --inventory-file=./hosts -become ckan.yml
ansible-playbook --inventory-file=./hosts -become virtuoso.yml
