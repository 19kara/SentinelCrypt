# src/crypto/aes_engine.py

from cryptography.fernet import Fernet

# Génération d'une clé (à stocker ailleurs en pratique)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data: bytes) -> bytes:
    """Chiffre des données avec AES (via Fernet)"""
    return cipher.encrypt(data)

def decrypt_data(token: bytes) -> bytes:
    """Déchiffre des données"""
    return cipher.decrypt(token)
