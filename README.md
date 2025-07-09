# Multi-Token Sender Script For Arbitrum Sepolia Network

This Python script automates the process of sending **multiple ERC-20 tokens** from **multiple sender wallets** to a **single recipient** on the **Arbitrum Sepolia testnet**.

## ✅ Features
- Sends *all available*  token balances from each wallet.
- Supports multiple ERC-20 token contracts.
- Handles errors and logs progress clearly in the terminal.
- Uses `.env` for secure configuration.

---

## 📦 Requirements

Make sure you have:

- Python 3.7+
- pip
- ARB Sepolia RPC endpoint (you can get from https://www.infura.io)
If you don't have this, steps on how you can do it will be at the bottom of this file.

Then install dependencies:

```bash
pip install web3 python-dotenv (enter this command on your terminal)
```

---

## ⚙️ Setup

1. **Clone or download this repo** to your local machine.

2. **Edit the `env.example` file and rename it to `.env`** in the same directory as the script by putting your RPC endpoint, address and private keys where necessary

> ⚠️ **Never share your `.env` file or private keys publicly!!**

---

## 🧾 Configure Tokens

In the script (`index.py`), there's a list of token contract addresses:

```python
token_addresses = [
    "0xTokenAddress1",
    "0xTokenAddress2",
    ...
]
```

Replace these with the token contracts you want to send.

---

## 🚀 Run the Script

Once your `.env` is set up and dependencies are installed, run:

```bash
python index.py (enter this command on your terminal)
```

The script will:
- Loop through each sender
- Check all token balances
- Send all available tokens to the recipient
- Log all actions and errors in the terminal

---

## 🛠️ Customize

- To **change the network**, update the `ARBITRUM_SEPOLIA_RPC` URL in `.env`.
- To **add/remove wallets or tokens**, just update the `.env` file and token list.
- To **adjust gas settings**, tweak this section in the script:

```python
"gas": 100000,
"gasPrice": w3.to_wei("0.01", "gwei"),
```

---

## ❓Troubleshooting

- `Could not connect to RPC`: Check if your RPC URL is valid and working.
- `Error sending token...`: Check token contract, gas settings, and private key.
- `Nonce too low`: Wait a few seconds or increase the delay between transactions.

---


## Steps on installing necessary packages
# First follow these steps to get your RPC endpoint;
- Visit https://www.infura.io
- Signup or login if you have an existing account
- Scroll a little down, if you see - `My First key, click on it`. If not, click on generate new API key
- By default, all chains are enabled, disable all except `Arbitrum Sepolia`. (If you want to use any other chain, simply enable it)
- Filter to `Active Endpoints` and then copy the URL under Arbitrum Sepolia. This URL is your RPC endpoint.

# To install python, follow these steps:
For Ubuntu/Linux, enter this command;
`sudo apt update`
`sudo apt install python3 python3-pip -y`
For MacOS, if you have homebrew installed, enter this command;
`brew install python`
For Windows;
- Go to `https://www.python.org/downloads/`
- Download the latest Python version
- Run the installer and make sure to check the box that says `Add Python to PATH`
- Then click `Install Now`

Alternatively, you can get python for your various operating sysytems on `https://www.python.org/downloads/`
- To check if python is installed `python --version` or `python3 --version`
- To check pip `pip --version` or `pip3 --version`

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---