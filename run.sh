#!/bin/bash

ansible ckan --inventory-file=./ansible_hosts -u vagrant -m ping
ansible ckan --inventory-file=./ansible_hosts -u vagrant -m shell -a 'uname -a'
ansible-playbook --inventory-file=./ansible_hosts -become ckan.yml
