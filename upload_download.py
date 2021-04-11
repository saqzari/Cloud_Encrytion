import googleDrive
import encrypt
import magic

g = googleDrive
e = encrypt
mime = magic.Magic(mime=True)


def check_file(file_name):
    result = g.searchFile(100, "name = \"" +  file_name + "\"")
    if result == 0:
        return 0
    else:
        return 1

def upload_encrypted(file_name):
    key = e.load_key()
    e.encrypt(file_name, key)
    g.uploadFile(file_name, file_name, mime.from_file(file_name))
    e.decrypt(file_name, key)

def download_decrypted_group(file_name):
    key = e.load_key()
    result = g.searchFile(100, "name = \"" + file_name + "\"")
    g.downloadFile(result[1], file_name)
    e.decrypt(file_name, key)

def download_decrypted_other(file_name):
    result = g.searchFile(100, "name = \"" + file_name + "\"")
    g.downloadFile(result[1], file_name)






