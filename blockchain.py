#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:32:17 2019
General Purpose Blockchain
Version: 1.0.0
@author: davidhill
"""


import datetime
import hashlib
import json
from flask import Flask
import jsonify

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, prev_hash = '0')
        
        
    def create_block(self, proof, prev_hash):
        block = {'index': len(self.chain + 1), 
                 'timestamp': str(datetime.datetime.now()), 
                 'proof': proof, 
                 'prev_hash': previous_hash}
        self.chain.append(block)
        return block
        
    


