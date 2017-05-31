#!/bin/bash
cd /mnt/web_data/caddy_www/;
sudo -H pip3 install -r requirements.txt;
make html;
