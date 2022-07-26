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
