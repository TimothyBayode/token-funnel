# index.py
# Copyright (c) 2025 Timothy Bayode
# Licensed under the MIT License. See LICENSE file for details.

# -*- coding: utf-8 -*-

from web3 import Web3
from dotenv import load_dotenv
import os
import json
import time

# Load environment variables
load_dotenv()

# Connect to the Arbitrum Sepolia network RPC
w3 = Web3(Web3.HTTPProvider(os.getenv("ARBITRUM_SEPOLIA_RPC")))
if not w3.is_connected():
    raise Exception("❌ Could not connect to Arbitrum Sepolia RPC.")

# ERC-20 ABI with required functions
ERC20_ABI = json.loads("""
[
    {"constant":true,"inputs":[{"name":"_owner","type":"address"}],
     "name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},
    {"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],
     "name":"transfer","outputs":[{"name":"","type":"bool"}],"type":"function"},
    {"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"},
    {"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"}
]
""")

# Get recipient address
recipient = os.getenv("RECIPIENT")

# Get token contract address. Make sure they are valid under the network you are using
token_addresses = [
    "0xContractAddress1",
    "0xContractAddress2",
    "0xContractAddress3",
    "0xContractAddress4",
    "0xContractAddress5",
    "0xContractAddress6",
    "0xContractAddress7",
    "0xContractAddress8"
]
# You can add or remove as many tokens in this order

# Preparing the sender wallets
wallets = [
    {
        "address": os.getenv("SENDER1_ADDRESS"),
        "private_key": os.getenv("SENDER1_PRIVATE_KEY")
    },
    {
        "address": os.getenv("SENDER2_ADDRESS"),
        "private_key": os.getenv("SENDER2_PRIVATE_KEY")
    },
    {
        "address": os.getenv("SENDER3_ADDRESS"),
        "private_key": os.getenv("SENDER3_PRIVATE_KEY")
    },
    {
        "address": os.getenv("SENDER4_ADDRESS"),
        "private_key": os.getenv("SENDER4_PRIVATE_KEY")
    },
]
# Make sure the number of senders tally with the number in .env file. For example if there are 5 sender wallets in .env file, then there should be 5 sender wallets in index.py

# Looping through each wallets and tokens
for wallet in wallets:
    sender = wallet["address"]
    pk = wallet["private_key"]
    print(f"\n🔄 Processing wallet: {sender}")

    for token_address in token_addresses:
        try:
            contract = w3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)
            symbol = contract.functions.symbol().call()
            decimals = contract.functions.decimals().call()
            raw_balance = contract.functions.balanceOf(sender).call()
            human_balance = raw_balance / (10 ** decimals)

            if raw_balance > 0:
                print(f"🪙 {symbol}: {human_balance:.4f} to send")

                nonce = w3.eth.get_transaction_count(sender)

                # Preparing the transfer transaction  on the blockchain
                tx = contract.functions.transfer(recipient, raw_balance).build_transaction({
                    "chainId": 421614, #ARB Sepolia chain id
                    "from": sender,
                    "nonce": nonce,
                    "gas": 120000,  # default cap for fallback
                    "maxFeePerGas": w3.to_wei(300, "gwei"),
                    "maxPriorityFeePerGas": w3.to_wei(50, "gwei")
                })

                # Try to estimate gas (is not always necessary)
                try:
                    tx["gas"] = w3.eth.estimate_gas(tx)
                except:
                    pass  # fallback to default amount if estimation fails

                signed_tx = w3.eth.account.sign_transaction(tx, private_key=pk)
                tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
                print(f"✅ Sent {human_balance:.4f} {symbol} | TX: https://sepolia.arbiscan.io/tx/{tx_hash.hex()}")

            else:
                print(f"⚠️ No {symbol} balance in wallet.")

        except Exception as e:
            print(f"❌ Error sending token at {token_address} from {sender}: {str(e)}")

        time.sleep(3)
