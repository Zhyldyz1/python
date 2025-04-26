from cryptography.fernet import Fernet
import os

# --------------------------
# 1. Generate or load the key
# --------------------------

def load_key():
    """Loads the key from file or creates one if it doesn't exist."""
    if os.path.exists("vault.key"):
        with open("vault.key", "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open("vault.key", "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
cipher = Fernet(key)

# --------------------------
# 2. Store an encrypted password
# --------------------------

def store_password(service, password):
    encrypted_password = cipher.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{service}:{encrypted_password.decode()}\n")
    print(f"[+] Stored encrypted password for {service}")

# --------------------------
# 3. Retrieve and decrypt
# --------------------------

def retrieve_password(service_name):
    with open("passwords.txt", "r") as file:
        for line in file:
            service, encrypted = line.strip().split(":")
            if service == service_name:
                decrypted = cipher.decrypt(encrypted.encode()).decode()
                print(f"[✓] Password for {service}: {decrypted}")
                return
    print("[!] Service not found.")

# --------------------------
# 💡 Example usage
# --------------------------

# Store passwords (run this once)
store_password("gmail", "myGmailPass123")
store_password("github", "g1tHubROck$")

# Retrieve them
retrieve_password("gmail")
retrieve_password("github")
