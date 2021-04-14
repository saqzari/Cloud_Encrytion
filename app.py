import userCommands
import adminCommands
import account

u = userCommands
a = adminCommands
acc = account


def main_menu():
    menu_running = 1
    print("\nWelcome to the Cloud! Enter:"
            + "\n'l' - if you want to login"
            + "\n'c'-  if you want to create an account"
            + "\n'e' - Exit\n")

    while menu_running == 1:
         user_input = input("\nEnter Sign In Command: ").lower()

         if(user_input == "l"):
            result = acc.login()

            if(result[0] == 0):
                menu_running = 0

            elif(result[0] == 1):
                u.user_console(result[1])

            elif(result[0] == 2):
                a.admin_console()


         elif(user_input == "c"):
            acc.create_account()

         elif(user_input == "e"):
            menu_running = 0

         elif(user_input == "h"):
            print("\nWelcome to the Cloud! Enter:"
            + "\n'l' - if you want to login"
            + "\n'c'-  if you want to create an account"
            + "\n'e' - Exit\n")

         
main_menu()


