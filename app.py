##########################
# Library & Module Imports
##########################
import streamlit as st
from pathlib import Path
import pandas as pd
import os
import json
from dotenv import load_dotenv
from web3 import Web3
from web3 import EthereumTesterProvider
# import deployer

# Load .env for URI & Cotract Address
load_dotenv()

####################
# Web 3 Connection
###################
# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
################################################################################


# Define the load_contract function
@st.cache(allow_output_mutation=True, hash_funcs={'_json.Scanner': lambda _: None})
def load_reward():

    # Load reward
   with open(Path("./contracts/compiled/reward_abi.json")) as f:
       import_abi = json.load(f)

   # Set the contract address (this is the address of the deployed contract)
   contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

   # Get the contract
   contract = w3.eth.contract(
       address=contract_address,
       abi=import_abi
   )
   # Return the contract from the function
   return contract

# Load the contract
reward_instance = load_reward()


# Load NFT
@st.cache(allow_output_mutation=True, hash_funcs={'_json.Scanner': lambda _: None})
def load_NFT():

    # Load reward
   with open(Path("./contracts/compiled/NFT721_abi.json")) as f:
       import_abi = json.load(f)

   # Set the contract address (this is the address of the deployed contract)
   contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

   # Get the contract
   contract = w3.eth.contract(
       address=contract_address,
       abi=import_abi
   )
   # Return the contract from the function
   return contract

# Load the contract
nft721_instance = load_NFT()


# Load RSVP
@st.cache(allow_output_mutation=True, hash_funcs={'_json.Scanner': lambda _: None})
def load_RSVP():

    # Load reward
   with open(Path("./contracts/compiled/rsvp_abi.json")) as f:
       import_abi = json.load(f)

   # Set the contract address (this is the address of the deployed contract)
   contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

   # Get the contract
   contract = w3.eth.contract(
       address=contract_address,
       abi=import_abi
   )
   # Return the contract from the function
   return contract

# Load the contract
rsvp_instance = load_RSVP()


# Load Staking
@st.cache(allow_output_mutation=True, hash_funcs={'_json.Scanner': lambda _: None})
def load_staking():

    # Load reward
   with open(Path("./contracts/compiled/stake_abi.json")) as f:
       import_abi = json.load(f)

   # Set the contract address (this is the address of the deployed contract)
   contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

   # Get the contract
   contract = w3.eth.contract(
       address=contract_address,
       abi=import_abi
   )
   # Return the contract from the function
   return contract

# Load the contract
staking_instance = load_staking()


# Load Safe
@st.cache(allow_output_mutation=True, hash_funcs={'_json.Scanner': lambda _: None})
def load_safe():

    # Load reward
   with open(Path("./contracts/compiled/eventSafeABI.json")) as f:
       import_abi = json.load(f)

   # Set the contract address (this is the address of the deployed contract)
   contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

   # Get the contract
   contract = w3.eth.contract(
       address=contract_address,
       abi=import_abi
   )
   # Return the contract from the function
   return contract

# Load the contract
eventSafe_instance = load_safe()


####################
# Streamlit Layout #
####################
## Two Button: - sidbar
# Create event
    # Mint NFT 721 - needs account
    # Ask event details
        # Event Name
        # End time 
        # Stake     
# RSVP
    # Ask which event:
        # Mint 720
        # Stake 
        # Check balance
        # Provide user pool access 
        # Cancellation

###########################
# Streamlit Interface code.
###########################

# Cover Image & Titles
st.image("Resources/hero.png")
st.title("G4 Event Staking Platform")
st.markdown("## Register or Create an Event")


# Event Button
with st.sidebar:
    st.header('What would you like to do?')
    if st.button("Create Event"):

        # Setting details
        with st.form("eventDetails"):
            event_name = st.text_input('Event Name')
            creator = st.text_input('ETH Wallet Address')
            time_end = st.text_input("Event Length (sec)")
            _stake = st.text_input("Enter stake")
            
            submitted = st.form_submit_button('Create')
if submitted:
    st.write(rsvp_instance.RSVP_Create(event_name, time_end, _stake))

    
eventFilter = contract.events.Appraisal.createFilter(
    fromBlock=0,
    argument_filters={"tokenId": token_id}
)
event = filter.get_all_entries()
for appraisal in appraisals:
    print(dict(appraisal))
# if st.button("RSVP for an Event"):
        
#transaction_hash = send_transaction(w3, creator, art_address)#
# ADD NFT FUNCT
# st.text("NFT Transferred to your address")
# display event status


#if st.button("RSVP"):
# event_name, time_end, _stake
# depositor = st.text_input('ETH Wallet Address')


#st.button("RSVP for an Event")



#######################
# Python Module Import
######################

# Import upcoming_events.csv
# upcoming_events = pd.read_csv(Path("Resources/Upcoming_events.csv"))
# upcoming_events = upcoming_events.drop(columns="Unnamed: 0")

# # Create events in CSV as individual variables.
# Event_1 = f"{upcoming_events.iloc[0,0]}"
# Event_2 = f"{upcoming_events.iloc[0,1]}"
# Event_3 = f"{upcoming_events.iloc[0,3]}"
# Event_4 = f"{upcoming_events.iloc[0,4]}"








###########################
# User Functions
###########################

# # Create form for registering for events
# with st.form(key="reg_event"):
#     st.markdown("### Register for upcoming event here!")
#     user_address = st.text_input("Enter your public address")
#     user_name = st.text_input("Enter your UserName")
#     # user_event_selection = st.selectbox('Choose YOUR event:', [Event_1, Event_2, Event_3, Event_4])
#     user_purchase = st.number_input("RSVP Amount (In WEI)", min_value =0, value=0, step=1)
#     submitted = submit_button = st.form_submit_button(label="Submit Registration")

# # Payout reward token form & function
# st.sidebar.markdown("## Collect Reward Here")
# with st.sidebar.form(key="token_rewards"):
#     submitted = submit_button = st.form_submit_button(label="Reward! Thank you for attending!")

# # Cancel RSVP before event date
# with st.sidebar.form(key="burn_token"):
#     st.markdown('### Cancel RSVP')
#     amount = st.number_input("Enter RSVP To Withdraw:", step=1)
#     submitted = submit_button = st.form_submit_button(label='Withdraw registration')``


# ###########################
# # Admin Functions
# ###########################
# admin_account = os.getenv("ADMIN_PUBLIC_KEY")

# st.sidebar.markdown("## Administrator Functions")
# with st.sidebar.form(key="add_event"):
#     st.markdown("### Add New Event")
#     submitted = submit_button = st.form_submit_button(label= "Event registered")