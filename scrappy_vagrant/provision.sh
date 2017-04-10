#!/usr/bin/env bash

#Update repositories
sudo apt-get update

#Install scappy dependencies
sudo apt-get -y install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev


#Install python
sudo apt-get -y install python3 python3-dev

#Install Scrappy
pip install scrapy



