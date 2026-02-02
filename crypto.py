from cryptography.fernet import Fernet

# ✅ Guaranteed valid Fernet key (same for server & client)
KEY = b"QmVtS3dVb3pZc3N0V1hYV2ZtT2ZQYzZpTjZ1N3B3ZVQ="

cipher = Fernet(KEY)

def encrypt_message(message: str) -> bytes:
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message: bytes) -> str:
    return cipher.decrypt(encrypted_message).decode()
