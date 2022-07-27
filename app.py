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

####################
# Web 3 Connection
###################
# Define and connect a new Web3 provider
#w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Define the load_contract function
#@st.cache(allow_output_mutation=True)
#def load_contract():

    # Load RSVP Contract ABI
#    with open(Path("./contracts/compiled/RSVP_contract_abi.json")) as f:
#        rsvp_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
#    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
#    contract = w3.eth.contract(
#        address = contract_address,
#        abi = rsvp_abi
#    )
    # Return the contract from the function
#    return contract

# Load the contract
#contract = load_contract()

#######################
# Python Module Import
######################

# Import upcoming_events.csv
upcoming_events = pd.read_csv(Path("Resources/Upcoming_events.csv"))
upcoming_events = upcoming_events.drop(columns="Unnamed: 0")

# Create events in CSV as individual variables.
Event_1 = f"{upcoming_events.iloc[0,0]}"
Event_2 = f"{upcoming_events.iloc[0,1]}"
Event_3 = f"{upcoming_events.iloc[0,3]}"
Event_4 = f"{upcoming_events.iloc[0,4]}"


###########################
# Streamlit Interface code.
###########################

# Cover Image & Titles
st.image("Resources/hero.png")
st.markdown("# Event Staking")
st.markdown("## Register for an Event")

###########################
# User Functions
###########################

# Create form for registering for events
with st.form(key="reg_event"):
    st.markdown("### Register for upcoming event here!")
    user_address = st.text_input("Enter your public address")
    user_name = st.text_input("Enter your UserName")
    user_event_selection = st.selectbox('Choose YOUR event:', [Event_1, Event_2, Event_3, Event_4])
    user_purchase = st.number_input("RSVP Amount (In WEI)", min_value =0, value=0, step=1)
    submitted = submit_button = st.form_submit_button(label="Submit Registration")

# Payout reward token form & function
st.sidebar.markdown("## Collect Reward Here")
with st.sidebar.form(key="token_rewards"):
    submitted = submit_button = st.form_submit_button(label="Reward! Thank you for attending!")

# Cancel RSVP before event date
with st.sidebar.form(key="burn_token"):
    st.markdown('### Cancel RSVP')
    amount = st.number_input("Enter RSVP To Withdraw:", step=1)
    submitted = submit_button = st.form_submit_button(label='Withdraw registration')


###########################
# Admin Functions
###########################
admin_account = os.getenv("ADMIN_PUBLIC_KEY")

st.sidebar.markdown("## Administrator Functions")
with st.sidebar.form(key="add_event"):
    st.markdown("### Add New Event")
    submitted = submit_button = st.form_submit_button(label= "Event registered")