import googleDrive
import encrypt
import magic
import os.path
from os import path

g = googleDrive
e = encrypt
mime = magic.Magic(mime=True)


def check_file(file_name):
    result = g.searchFile(100, "name = \"" +  file_name + "\"")
    if result == 0:
        return 0
    else:
        return 1

def upload_encrypted():
    key = e.load_key()
    user_input = input("Input file to encrypt and upload to drive\n")

    if path.exists(user_input):
        e.encrypt(user_input, key)
        g.uploadFile(user_input, user_input, mime.from_file(user_input))
        e.decrypt(user_input, key)
        print("Upload completed")
    else:
        print("File doesn't exist")

    

def download_decrypted_group():
    key = e.load_key()
    user_input = input("Input file to download\n")
    if check_file(user_input) == 1:
        result = g.searchFile(100, "name = \"" + user_input + "\"")
        g.downloadFile(result[1], user_input)
        e.decrypt(user_input, key)
        print("Download completed")
    else:
        print("File doesn't exist")

def download_decrypted_other():
    user_input = input("Input file to download\n")
    if check_file(user_input) == 1:
        result = g.searchFile(100, "name = \"" + user_input + "\"")
        g.downloadFile(result[1], user_input)
        print("Download completed. \nNote: Since you are not part of the group, file is encrypted")
    else:
        print("File doesn't exist")





