from pathlib import Path
from cryptography.fernet import Fernet
import subprocess
import time
import os


""" Path to the key and encrypted password files"""

s_key_file = "secret.key"
s_enc_file = "encrypted_password.bin"

""" Check if the key and encrypted password files exist, if not, run keys.py to generate them"""

if not Path(s_key_file).is_file() or not Path(s_enc_file).is_file():
    print("Key or encrypted password file not found. Generating them...")
    subprocess.run(["python", "keys.py"])
else:
    print("Key and encrypted password file found. Proceeding to decrypt the password.")

""" Load key and encrypted password """

with open("secret.key", "rb") as key_file:

    key = key_file.read()

f = Fernet(key)

with open("encrypted_password.bin", "rb") as enc_file:

    encrypted = enc_file.read()

password = f.decrypt(encrypted).decode()

# Launch app

#subprocess.Popen(r"C:\DSN Software Inc\DSNSoftware\DSN.Exec.WPF.exe")

time.sleep(10)

# Send credentials

print('dsnadmin')

print('tab')

print(password)

print('enter')
print('enter')