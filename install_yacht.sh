#!/bin/bash
pip3 install -r /opt/SelfhostedPro/.requirements.txt
python3  /opt/SelfhostedPro/.install_yacht.py
/bin/cp /opt/SelfhostedPro/.bashrc /root/.bashrc
