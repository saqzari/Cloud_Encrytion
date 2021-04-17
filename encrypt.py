from cryptography.fernet import Fernet

# Generates a key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open("keys/key.key", "wb") as key_file:
        key_file.write(key)

# Loads the key from the current directory named `key.key`
def load_key():
    return open("keys/key.key", "rb").read()

# Given a filename (str) and key (bytes), it encrypts the file and write it
def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = f.encrypt(file_data)

    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Given a filename and key, it decrypts the file and writes it
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
