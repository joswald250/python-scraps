import usernames as u
import password_cache as pwc

'''class Password:
    def __init__(self, username, password):
        self.username = username
        self.password = add_password(self.username)'''

def check_user(username):
    i = 0
    my_list_of_usernames = u.list_of_usernames
    for i in range(0, len(my_list_of_usernames)):
        if my_list_of_usernames[i] == username:
            return True
        else:
            pass


def add_password(user, password):
    i = 0
    my_list_of_passwords = pwc.list_of_passwords
    my_list_of_usernames = u.list_of_usernames
    if check_user(user):
        print("Username already taken!")
        return False
    else:
        my_list_of_usernames.append(user)
        my_list_of_passwords.append(password)
        username_file = open('usernames.py', 'w')
        passwords_file = open('password_cache.py', 'w')
        username_file.write('list_of_usernames = ' + str(my_list_of_usernames))
        passwords_file.write('list_of_passwords = ' + str(my_list_of_passwords))
        username_file.close()
        passwords_file.close()
        return True

def validate_password(username, password):
    i = 0
    my_list_of_passwords = pwc.list_of_passwords
    my_list_of_usernames = u.list_of_usernames
    for i in range(0, len(my_list_of_usernames)):
        if my_list_of_usernames[i] == username:
            if my_list_of_passwords[i] == password:
                valid = True
                break
            else:
                valid = False
        else:
            valid = False
    return valid

