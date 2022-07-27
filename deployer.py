from web3 import Web3
from solcx import compile_source

import os
import json
from dotenv import load_dotenv
from web3 import Web3
from web3 import EthereumTesterProvider

# Load .env for URI & Cotract Address
load_dotenv()

"""
Establishing W3
Load accounts
    Reward Token
    NFT721
    RSVP
        address1
        address2
        owner
    Deploy the rest
"""
# @ TODO:
# 1. Add file path
# 2. Add place for tx storage
#       - Maybe ABI/Bin?
# 3. Hardcode / Pass w3


# Solidity source code 
def compile_source_file(file_path):
    with open(file_path, 'r') as f:
        source = f.read()

    return compile_source(source)
    #      output_values=['abi', 'bin']


# Adding function to deploy the compiled Solidity files
def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).constructor().transact()

    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address

# Initializing w3 connection
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))








# retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin
>>> bytecode = contract_interface['bin']

# get abi
>>> abi = contract_interface['abi']

# web3.py instance
>>> w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
>>> w3.eth.default_account = w3.eth.accounts[0]

>>> Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
>>> tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
>>> tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

>>> greeter = w3.eth.contract(
...     address=tx_receipt.contractAddress,
...     abi=abi
... )

>>> greeter.functions.greet().call()
'Hello'

>>> tx_hash = greeter.functions.setGreeting('Nihao').transact()
>>> tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
>>> greeter.functions.greet().call()
'Nihao'