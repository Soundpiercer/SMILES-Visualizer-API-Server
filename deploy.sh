#!/bin/sh
. /home/ubuntu/Documents/SMILES-Visualizer-API-Server/env/bin/activate
git pull origin main
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
sudo systemctl restart nginx
sudo systemctl restart gunicorn
