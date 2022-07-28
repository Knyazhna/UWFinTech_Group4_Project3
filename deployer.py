# Imports
from web3 import Web3
from solcx import compile_source

import sys
import os
import json
from dotenv import load_dotenv
from web3 import Web3
from web3 import EthereumTesterProvider

# Load .env for URI & Contract Address
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

# TODO:
# Add aacounts
# Add main
# Maybe seperate
# Add buttons
# Need to set parameters for a few 


# Solidity source code 
def compile_source_file(contract):
    with open("./contracts/" + contract + '.sol') as f:
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


# Adding contract list to generate filepaths
contractList = ['eventSafeME', 'Nft721ME', 'rewardTokenME', 'rsvpEventME', 'stakingME']
abiList = ['safeAbi', 'nft721Abi', 'rewardAbi','rsvpAbi']

def deploy(contractList, abiList):
    # Initializing list
    interfaceList = []

    # Recursive loading function
    for contract in range(len(contractList)):
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



# def fetch_abi():

#     contractList = [EVT_Token, CreatorERC721, RSVP_Event]
#     contractAbiList = ['tokenAbi', 'nftAbi', 'rsvpAbi']

#     for i in range(len(contractList)):
#         struct = {
#             "CONTRACT_ADDRESS": str(contractList[i][-1]),
#             "CONTRACT_ABI": contractList[i][-1].abi
#         }

#         with open(('./app/src/abi/' + contractAbiList[i] + '.json'), 'w', encoding='utf-8') as f:
#             json.dump(struct, f, indent=3)


# # set pre-funded account as sender
# >>> w3.eth.default_account = w3.eth.accounts[0]

# >>> Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

# # Submit the transaction that deploys the contract
# >>> tx_hash = Greeter.constructor().transact()

# # Wait for the transaction to be mined, and get the transaction receipt
# >>> tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# >>> greeter = w3.eth.contract(
# ...     address=tx_receipt.contractAddress,
# ...     abi=abi
# ... )

# >>> greeter.functions.greet().call()
# 'Hello'

# >>> tx_hash = greeter.functions.setGreeting('Nihao').transact()
# >>> tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# >>> greeter.functions.greet().call()
# 'Nihao'