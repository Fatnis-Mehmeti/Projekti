import hashlib
from cryptography.fernet import Fernet
# Function to generate a secure encryption key
def generate_key():
key = Fernet.generate_key()
with open(&#39;encryption_key.key&#39;, &#39;wb&#39;) as key_file:
key_file.write(key)
# Function to load the encryption key
def load_key():
with open(&#39;encryption_key.key&#39;, &#39;rb&#39;) as key_file:
key = key_file.read()
return key

# Function to encrypt data
def encrypt_data(data, key):
cipher_suite = Fernet(key)
encrypted_data = cipher_suite.encrypt(data.encode())
return encrypted_data

# Function to decrypt data
def decrypt_data(encrypted_data, key):
cipher_suite = Fernet(key)
decrypted_data = cipher_suite.decrypt(encrypted_data)
return decrypted_data.decode()

# Generate encryption key
generate_key()

# Load encryption key
key = load_key()

# Sensitive data to be protected
sensitive_data = &quot;This is a secret message!&quot;
# Encrypt the sensitive data
encrypted_data = encrypt_data(sensitive_data, key)
print(&quot;Encrypted Data:&quot;, encrypted_data)
# Decrypt the encrypted data
decrypted_data = decrypt_data(encrypted_data, key)
print(&quot;Decrypted Data:&quot;, decrypted_data)
