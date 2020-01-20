#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:28:34 2019
General Purpose Blockchain Miner
Version: 1.0.0
@author: davidhill
"""

from flask import Flask, jsonify
from blockchain import Blockchain


# Initialize web app
app = Flask(__name__)

#Create Blockchain
blockchain = Blockchain()

# Mine Block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    prev_block = blockchain.get_prev_block()
    prev_proof = prev_block['proof']
    proof = blockchain.proof_of_work(prev_proof)
    prev_hash = blockchain.hash(prev_block)
    block = blockchain.create_block(proof, prev_hash)
    response = {'message': 'Congradulations! You mined a block!', 
                'index': block['index'], 
                'timestamp': block['timestamp'], 
                'proof' : block['proof'], 
                'prev_hash': block['prev_hash']}
    return jsonify(response), 200

# Get Blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'chain_length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/test', methods=['GET'])
def test():
    return 200

@app.route('/is_valid', methods=['GET'])
def is_valid():
    if blockchain.is_valid(blockchain.chain):
        response = {'message': 'The blockchain is valid!'}
        return jsonify(response), 200
    
    else:
        response = {'message': 'The blockchain is NOT valid...'}
        return jsonify(response), 200

    
    
    

# Run app
app.run(host='0.0.0.0', port=5000)




