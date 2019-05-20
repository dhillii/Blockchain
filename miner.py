#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:28:34 2019
General Purpose Blockchain Miner
Version: 1.0.0
@author: davidhill
"""

from flask import Flask
import jsonify
from blockchain.py import Blockchain


# Initialize web app
app = Flask(__name__)

#Create Blockchain

blockchain = Blockchain()

