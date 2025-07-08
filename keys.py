from cryptography.fernet import Fernet
# Generate key once
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
   key_file.write(key)
# Use the key to encrypt the password
f = Fernet(key)
password = "*@!B)&DSN"
encrypted = f.encrypt(password.encode())
with open("encrypted_password.bin", "wb") as enc_file:
   enc_file.write(encrypted)
print("Encrypted password saved.")