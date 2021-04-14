import pickle
import account

a = account

def read():
    f = open('pickles/group.pickle', "a")
    f.close()
    with open('pickles/group.pickle', 'rb') as handle:
        try:
            group = pickle.load(handle)
        except EOFError:
            group = []
    return group

def write_back(group):
    with open('pickles/group.pickle', 'wb') as handle:
        pickle.dump(group, handle, protocol=pickle.HIGHEST_PROTOCOL)

def delete_from_group():
    group = read()
    user_input = input("Input user to add to delete from group\n")
    if check(user_input) == 1:
        group.remove(user_input)
        write_back(group)
        print("User has been removed from group")
    elif a.check(user_input) == 1:
        print("User exists but not part of group")
    else:
        print("This user does not exist")

def add_to_group():
    group = read()
    user_input = input("Input user to add to group\n")
    if check(user_input) == 1:
        print("This user is already in the group")
    elif a.check(user_input) == 1:
        group.append(user_input)
        write_back(group)
        print("User has been added")
    else:
        print("This user does not exist")

def get_from_group():
    group = read()
    print('\nGroup Members:')
    print('\n'.join(group))
    print('')

def check(user):
    group = read()
    if user in group:
        return 1
    return 0

