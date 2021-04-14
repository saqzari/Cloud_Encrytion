import pickle
import getpass

def read():
    f = open('pickles/users.pickle', "a")
    f.close()
    with open('pickles/users.pickle', 'rb') as handle:
        try:
            users = pickle.load(handle)
        except EOFError:
            users = []
    return users

def write_back(users):
    with open('pickles/users.pickle', 'wb') as handle:
        pickle.dump(users, handle, protocol=pickle.HIGHEST_PROTOCOL)

def delete_user():
    users = read()
    user_input = input("Input user to delete\n")
    if check(user_input) == 1:
        del users[user_input]
        write_back(users)
        print("User has been deleted")
    else:
        print("This user does not exist")

def get_users():
    users = read()
    print ("")
    print ("{:<8}        {:<10}".format('User Name:','Password:'))
    for user_name, passwd in users.items():
        print ("{:<8}          {:<10}".format(user_name, passwd))
    print ("")

def check(user):
    users = read()
    if user in users:
        return 1
    return 0

def create_account():
     users = read()
     while True:
        createLogin = input("\nCreate login name: ")
        if createLogin in users:
            print("\nLogin name already exist! Try again\n")
        else:
            createPassword = getpass.getpass("Create password: ")
            users[createLogin] = createPassword
            write_back(users)
            print("\nUser created\n")
            return 0

def login():
     users = read()
     attempts = 0;
     while True:
        input_user = input("\nInput login name: ")
        input_password = getpass.getpass("Input password: ")

        if input_user == 'admin' and input_password == '123':
            return [2, 'admin']

        elif input_user in users:
            if users[input_user] == input_password:
                 print("\nLogin successful!\n")
                 return [1, input_user]
            else:
                print("\nIncorrect password!\n")
                attempts = attempts + 1
        else:
            print("\nIncorrect user!\n")
            attempts = attempts + 1

            if attempts == 3:
                print("\nError! Too many attempts\n")
                return [0, 'none']
           


