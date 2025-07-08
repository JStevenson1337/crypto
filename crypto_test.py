from cryptography.fernet import Fernet
import subprocess
import time

# Load key and encrypted password

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