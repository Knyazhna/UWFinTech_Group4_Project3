# Imports
# must have solcx and web3 installed 
from importlib_metadata import version
from web3 import Web3
from solcx import compile_source

import solcx
import sys
import os
import json
from dotenv import load_dotenv
from web3 import Web3
from web3 import EthereumTesterProvider

# Load .env for URI & Contract Address
load_dotenv()

# attempt at solcx version solution 
# solcx.install_solc(version='0.8.9')
# solcx.set_solc_version('0.8.9')

# page visualization 
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

# TODO:
# Find source of compiling error, some issue with solcx
# interfaceList needed to connect to server.py 


# Solidity source code 
def compile_source_file(contract):
    solcx.install_solc(version='0.8.9')
    solcx.set_solc_version('0.8.9')
    with open("./Contracts/" + contract + '.sol') as f:
        source = f.read()
        print(source)
    source = "contract Foo {function bar() public {return; }}"
    return compile_source(source)
    
    # output_values=['abi', 'bin']


# Adding function to deploy the compiled Solidity files
def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).constructor().transact()

    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address


# Initializing w3 connection
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))


# Adding contract list to generate filepaths
def deploy():
    # Initializing list
    contractList = ['eventSafeME', 'Nft721ME', 'rewardTokenME', 'rsvpEventME', 'stakingME']
    abiList = ['safeAbi', 'nft721Abi', 'rewardAbi','rsvpAbi']
    interfaceList = []

    # Recursive loading function
    for contract in (contractList):
        # Compile source file
        compiled_sol = compile_source_file(contract)

        # Fetch contract interface and ID
        contract_id, contract_interface = compiled_sol.popitem()

        # bytecode = contract_interface['bin']
        # abi = contract_interface['abi']

        # Deploy contract
        address = deploy_contract(w3, contract_interface)

        # Saving interfaces for export
        interface = w3.eth.contract(address=address, abi=contract_interface["abi"])
        interfaceList.append(interface)

        struct = {
                "CONTRACT_ADDRESS": address,
                "CONTRACT_ABI": contract_interface['abi'].abi
            }

        # Adding json file  
        with open(('./compiled/' + abiList[contract] + '.json'), 'w', encoding='utf-8') as f:
            json.dump(struct, f, indent=3)
        

        print(f'Deployed {contract_id} to: {address}\n')
        # gas_estimate = store_var_contract.functions.setVar(255).estimate_gas()
        # print(f'Gas estimate to transact with setVar: {gas_estimate}')

        return interfaceList



# Once interfaceList is gathered, connect them to appropriate actions in server.py where params still need to be set