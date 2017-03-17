#!/bin/bash

ssh-copy-id -i ~/.ssh/id_rsa.pub vagrant@192.168.33.10
ansible ckan --inventory-file=./ansible_hosts -u vagrant -m ping
ansible ckan --inventory-file=./ansible_hosts -u vagrant -m shell -a 'uname -a'
ansible-playbook --inventory-file=./ansible_hosts -become ckan.yml
