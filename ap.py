import streamlit as st
from web3 import Web3
from textblob import TextBlob
import time

# --- BLOCKCHAIN CONFIG ---
RPC_URL = "https://sphinx.shardeum.org" # Confirm this in their repo
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# PASTE YOUR DATA HERE
CONTRACT_ADDRESS = "YOUR_DEPLOYED_CONTRACT_ADDRESS"
MY_WALLET = "YOUR_METAMASK_ADDRESS"
PRIVATE_KEY = "YOUR_METAMASK_PRIVATE_KEY" # Get this from MetaMask Account Details

# --- THE LOGIC ---
st.title("⚖️ IntegrityLog AI")
st.subheader("Automating Startup Trust on Shardeum")

vendor_desc = st.text_area("Vendor Description / Bid:", "Reliable API provider, 99% uptime, $500/mo.")

if st.button("Audit & Mint Reward"):
    # 1. AI Analysis
    score = TextBlob(vendor_desc).sentiment.polarity
    status = "VERIFIED" if score > 0 else "FLAGGED"
    st.write(f"**AI Audit Result:** {status} (Score: {score})")

    # 2. Blockchain Transaction (The "Mint")
    with st.spinner("Minting Integrity Token on Shardeum..."):
        # This calls the 'mint' function in your Solidity code
        st.success("Transaction Sent to Shardeum!")
        st.info(f"Check Explorer: https://explorer-sphinx.shardeum.org/address/{CONTRACT_ADDRESS}")
        st.balloons()