import upload_download
import group
import account
import googleDrive
import sys

u = upload_download
g = group
a = account
gd = googleDrive

def user_console(user_name):
    menu_running = 1 
    print("\nWelcome " + user_name + "!\nCommands:"   
            + "\n'up'- Upload settings"  
            + "\n'd' - Download settings"
            + "\n'h' - Help"
            + "\n'l' - Log out"
            + "\n'e' - Exit to Sign In\n")
    
    while menu_running == 1:
         user_input = input("\nEnter Main Command: ").lower()

         if(user_input == "up"):
            if g.check(user_name) == 1:
                upload_settings()
            else:
                print("You're not part of the group")

         elif(user_input == "d"):
            download_settings(user_name)

         elif(user_input == "h"):
            print("\nCommands:"   
            + "\n'up'- Upload settings" 
            + "\n'd' - Download settings"
            + "\n'h' - Help"
            + "\n'l' - Log out"
            + "\n'e' - Exit to Sign In\n")

         elif(user_input == "l"):
            sys.exit()

         elif(user_input == "e"):
            menu_running = 0


def upload_settings():
    upload_running = 1
    print("\nUpload Commands:"
            + "\n'u' - Upload file"  
            + "\n'v'-  View all files"
            + "\n'h' - Help"
            + "\n'e' - Exit to main menu\n")
    while upload_running == 1:
        user_input = input("Enter Upload Command: ").lower()

        if(user_input == "u"):
            u.upload_encrypted()

        elif(user_input == "v"):
            gd.listFiles(100)

        elif(user_input == "h"):
            print("\nUpload Commands:"
            + "\n'u' - Upload file"  
            + "\n'v'-  View all files"
            + "\n'h' - Help"
            + "\n'e' - Exit to main menu\n")

        elif(user_input == "e"):
            upload_running = 0

def download_settings(user_name):
    download_running = 1
    print("\nDownload Commands:"
            + "\n'd' - Download file"  
            + "\n'v'-  View all files"
            + "\n'h' - Help"
            + "\n'e' - Exit to main menu\n")
    while download_running == 1:
        user_input = input("Enter Download Command: ").lower()

        if(user_input == "d"):
            if g.check(user_name) == 1:
                u.download_decrypted_group()
            else:
                u.download_decrypted_other()

        elif(user_input == "v"):
            gd.listFiles(100)

        elif(user_input == "h"):
            print("\nDownload Commands:"
            + "\n'd' - Download file"  
            + "\n'v'-  View all files"
            + "\n'h' - Help"
            + "\n'e' - Exit to main menu\n")

        elif(user_input == "e"):
            download_running = 0

