# Library & Module Imports
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

    submitted = submit_button = st.form_submit_button(label="Submit Registration")