"""Merchant accounts."""
import hashlib


def hash_password(password: str) -> str:
    """Hash stored for a merchant's dashboard password."""
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(password: str, stored: str) -> bool:
    return hash_password(password) == stored


def create_account(store: dict, merchant: str, password: str) -> None:
    if merchant in store:
        raise ValueError("merchant already exists")
    store[merchant] = hash_password(password)


def login(store: dict, merchant: str, password: str) -> bool:
    stored = store.get(merchant)
    return stored is not None and verify_password(password, stored)
