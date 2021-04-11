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
    print("\nCommands:" 
            + "\n'g' - group settings"  
            + "\n'up'- Upload settings" 
            + "\n'u' - User settings" 
            + "\n'd' - Download settings"
            + "\n'h' - Help"
            + "\n'l' - Log out"
            + "\n'e' - Exit\n")
    
    while menu_running == 1:
         user_input = input().lower()
         
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
            + "\n'e' - Exit\n")

         elif(user_input == "l"):
            sys.exit()

         elif(user_input == "e"):
            menu_running = 0

def group_settings():  
    user_input = input("\nGroup Commands: \n'a' - add user"  
            + "\n'r'-  Remove from group" 
            + "\n'v' - View members of group" 
            + "\n'u' - View all available users\n").lower()

    if(user_input == "a"):
        g.add_to_group()

    elif(user_input == "r"):
        g.delete_from_group()

    elif(user_input == "v"):
        g.get_from_group()

    elif(user_input == "u"):
        a.get_users()

def user_settings():  
    user_input = input("\nUser Commands: \n'c' - Create user"  
            + "\n'd'-  Delete user" 
            + "\n'v' - View all users\n").lower()

    if(user_input == "c"):
        a.create_account()

    elif(user_input == "d"):
        a.delete_user()

    elif(user_input == "v"):
        a.get_users()

def upload_settings():
    user_input = input("\nUpload Commands:"
            + "\n'u' - Upload file"  
            + "\n'v'-  View all files\n").lower()

    if(user_input == "u"):
        pass

    elif(user_input == "v"):
        gd.listFiles(100)

def download_settings():
    user_input = input("\nDownload Commands:"
            + "\n'd' - Download file"  
            + "\n'v'-  View all files\n").lower()

    if(user_input == "d"):
        pass

    elif(user_input == "v"):
        gd.listFiles(100)

admin_console()
