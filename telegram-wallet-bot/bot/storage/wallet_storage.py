# storage/wallet_storage.py
import json
import os
from pathlib import Path


class WalletStorage:
    def __init__(self, path: str = "data/wallets.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._data = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            with open(self.path, "r") as f:
                return json.load(f)
        return {}

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=2)

    def save_wallet(self, user_id: int, wallet: dict):
        self._data[str(user_id)] = wallet
        self._save()

    def get_wallet(self, user_id: int) -> dict | None:
        return self._data.get(str(user_id))