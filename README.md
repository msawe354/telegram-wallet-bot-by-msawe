# Crypto Wallet Bot

Telegram bot for creating and managing Ethereum wallets. Built with Python, aiogram, and AES-256-GCM encryption.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python)
![aiogram](https://img.shields.io/badge/aiogram-3.x-2CA5E0?logo=telegram)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Overview

Crypto Wallet Bot is a Telegram bot that lets users create and manage Ethereum wallets directly in chat. Private keys are encrypted with a user-provided password using AES-256-GCM and PBKDF2 key derivation. Keys are never stored in plaintext.

---

## Features

- Create a new Ethereum wallet
- Import wallet from private key
- Password-based encryption (AES-256-GCM + PBKDF2, 100k iterations)
- Wallet address lookup
- Balance check (address only)
- Send crypto (coming soon)
- Export private key (coming soon)

---

## Project Structure
telegram-wallet-bot/
├── bot/
│ ├── init.py
│ ├── main.py
│ ├── routers.py
│ └── handlers/
│ ├── init.py
│ ├── start.py
│ ├── wallet.py
│ ├── balance.py
│ ├── send.py
│ ├── import_wallet.py
│ └── settings.py
├── config/
│ ├── init.py
│ └── settings.py
├── services/
│ ├── init.py
│ └── wallet_service.py
├── storage/
│ ├── init.py
│ └── wallet_storage.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
text


---

## Requirements

- Python 3.10+
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Ethereum RPC URL (default: `https://eth.llamarpc.com`)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/telegram-wallet-bot.git
cd telegram-wallet-bot

2. Install dependencies
bash

pip install -r requirements.txt

3. Configure environment
bash

cp .env.example .env

Edit .env and add your bot token:
text

BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
ETH_RPC_URL=https://eth.llamarpc.com

4. Run the bot
bash

python -m bot.main

Usage
Commands
Command	Description
/start	Show welcome message
/wallet	Create a new wallet
/import	Import wallet from private key
/balance	Show wallet address
/send	Send crypto (coming soon)
/settings	Wallet settings
/export	Export private key (coming soon)
Security

    Private keys are encrypted with AES-256-GCM

    Key derivation uses PBKDF2-HMAC-SHA256 with 100,000 iterations

    Password is never stored anywhere

    Each wallet has a unique random salt and nonce

    .env file is excluded from Git via .gitignore

Warning: Never share your private key or password with anyone. The bot never sends private keys over the network.
Tech Stack
Component	Technology
Language	Python 3.10+
Bot Framework	aiogram 3.x
Cryptography	cryptography (AES-256-GCM, PBKDF2)
Ethereum	eth-account, web3
Storage	JSON file
Roadmap
Version	Features
v0.1	✅ Wallet creation, import, encryption
v0.2	🔜 Balance check via RPC
v0.3	🔜 Send ETH transactions
v0.4	🔜 Export private key
v1.0	🔜 Multi-chain support (BSC, Polygon, TON)
