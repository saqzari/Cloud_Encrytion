import upload_download
import group
import account
import googleDrive
import sys

u = upload_download
g = group
a = account
gd = googleDrive


def admin_console():
    menu_running = 1
    print("\nWelcome Admin!\nCommands:"
            + "\n'g' - group settings"
            + "\n'up'- Upload settings"
            + "\n'u' - User settings"
            + "\n'd' - Download settings"
            + "\n'h' - Help"
            + "\n'l' - Log out"
            + "\n'e' - Exit to Sign In\n")

    while menu_running == 1:
         user_input = input("\nEnter Main Command: ").lower()

         if(user_input == "g"):
            group_settings()

         elif(user_input == "up"):
            upload_settings()

         elif(user_input == "u"):
            user_settings()

         elif(user_input == "d"):
            download_settings()

         elif(user_input == "h"):
            print("\nCommands:"
            + "\n'g' - group settings"
            + "\n'up'- Upload settings"
            + "\n'u' - User settings"
            + "\n'd' - Download settings"
            + "\n'h' - Help"
            + "\n'l' - Log out"
            + "\n'e' - Exit to Sign In\n")

         elif(user_input == "l"):
            sys.exit()

         elif(user_input == "e"):
            menu_running = 0


def group_settings():
    group_running = 1
    print("\nGroup Commands: \n'a' - add user"
                + "\n'r'-  Remove from group"
                + "\n'v' - View members of group"
                + "\n'u' - View all available users"
                + "\n'h' - Help"
                + "\n'e' - Exit to main menu\n")
    while group_running == 1:
        user_input = input("Enter Group Command: ").lower()

        if(user_input == "a"):
            g.add_to_group()

        elif(user_input == "r"):
            g.delete_from_group()

        elif(user_input == "v"):
            g.get_from_group()

        elif(user_input == "u"):
            a.get_users()

        elif(user_input == "h"):
            print("\nGroup Commands: \n'a' - add user"  
                + "\n'r'-  Remove from group" 
                + "\n'v' - View members of group" 
                + "\n'u' - View all available users"
                + "\n'h' - Help"
                + "\n'e' - Exit to main menu\n")

        elif(user_input == "e"):
            group_running = 0

def user_settings():  
    user_running = 1
    print("\nUser Commands: \n'c' - Create user"  
            + "\n'd'-  Delete user" 
            + "\n'v' - View all users"
            + "\n'h' - Help"
            + "\n'e' - Exit to main menu\n")
    while user_running == 1:
        user_input = input("Enter User Command: ").lower()

        if(user_input == "c"):
            a.create_account()

        elif(user_input == "d"):
            a.delete_user()

        elif(user_input == "v"):
            a.get_users()

        elif(user_input == "h"):
            print("\nUser Commands: \n'c' - Create user"  
            + "\n'd'-  Delete user" 
            + "\n'v' - View all users"
            + "\n'h' - Help"
            + "\n'e' - Exit to main menu\n")

        elif(user_input == "e"):
            user_running = 0

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

def download_settings():
    download_running = 1
    print("\nDownload Commands:"
            + "\n'd' - Download file"  
            + "\n'v'-  View all files"
            + "\n'h' - Help"
            + "\n'e' - Exit to main menu\n")
    while download_running == 1:
        user_input = input("Enter Download Command: ").lower()

        if(user_input == "d"):
            u.download_decrypted_group()

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

