#!/bin/bash

ansible ckan --inventory-file=./ansible_hosts -u vagrant -m ping
