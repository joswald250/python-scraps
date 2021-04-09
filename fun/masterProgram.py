import getpass
import sys
import os
import random
import passwords as pw
import keyboard
import urllib.request
import webbrowser
from urllib.parse import urlparse


def websearch():
    url = ''
    while True:
        user_input = str(input('What website would you like to visit?'))
        if user_input == '':
            user_input = str(input('What website would you like to visit?'))
        else:
            break

    parse = urlparse(user_input)
    scheme = parse.scheme
    netloc = parse.netloc
    path = parse.path
    params = parse.params
    query = parse.query
    fragment = parse.fragment

    # if it is google.com or youtube.com
    if (scheme == '') and (netloc == ''):
        position = path.find('.com')
        netloc = path[:position + 4]
        path = path[position + 4:]
        # print('if 1 ran')

    # if it finds no https
    if scheme.find('https') < 0:
        scheme = "https"
        # print('if 2 ran')

    # if there is no w. at all in the netloc, it places a www. at the front
    if netloc.find('w.') < 0:
        netloc = 'www.' + netloc
        # print('if 3 ran')

    # if netloc does not include a 'w.com' and does have a 'ww.' or 'w.' should replace the first 'w.' or 'ww.' with
    # 'www.' aka ww.google.com or w.google.com
    if ((netloc.find('w.com') < 0 and netloc.find('www.') < 0 and netloc.find('ww.') >= 0) or
            (netloc.find('w.com') < 0 and netloc.find('www.') < 0 and netloc.find('w.') >= 0)):
        position = netloc.find('w.')
        netloc = 'www.' + netloc[position + 2:]
        # print('if 4 ran')

    # if netloc has w.com and w. or ww., erase either instance and replace with www. aka w.flow.com
    if ((netloc.find('w.com') >= 0 and netloc.find('ww.') >= 0 and netloc.find('www.') < 0) or
            (netloc.find('w.com') >= 0 and netloc.find('w.') >= 0 and netloc.find('www.') < 0 and (
                    netloc.find('w.') < netloc.find('w.com')))):
        position = netloc.find('w.')
        netloc = 'www.' + netloc[position + 2:]
        # print('if 5 ran')
    # if netloc has 'w.com' but no 'www.' or 'ww.' or 'w.' it adds 'www.' aka flow.com
    elif ((netloc.find('w.com') >= 0 and netloc.find('www.') < 0) or (
            netloc.find('w.com') >= 0 and netloc.find('ww.') < 0) or
          (netloc.find('w.com') >= 0 and (netloc.find('w.') > netloc.find('w.com')))):
        netloc = "www." + netloc
        # print('if 6 ran')

    if netloc.rfind('.') < (len(netloc) - 4):
        print('Please include an ending (.com, .edu, .gov, etc...) to your net location.')
        # in master program insert: return
        # print('if 7 ran')
        return

    url = scheme + '://' + netloc + path + params + query + fragment

    # requests the actual website
    website = urllib.request.urlopen(url)
    webbrowser.open(url, new=2)
    print('result code: ' + str(website.getcode()))

    store_data_question = str(input('Would you like to save the website data to a file? (Enter: yes or no)'))
    if store_data_question == 'yes':
        file_location_input = str(input('What would you like to name the file?'))
        website_data = website.read()
        file = open(file_location_input, 'w+')
        file.write(str(website_data))
        file.close()


def guessing_game():
    randomNum = random.randint(1, 100)
    print('{}, I am thinking of a number, guess away! (you have 5 guesses)'.format(username))

    correct = False
    for guessNum in range(5):
        try:
            guess = int(input("Whaddaya think?"))
        except ValueError:  # in case they input a non-integer
            print('Please enter a number value, not text.')

        try:
            if guess == randomNum:
                print("Wow, right on target!")
                correct = True
                break
            elif guess > randomNum:
                print('Too high!')
            else:
                print('Too low!')
        except NameError:
            print('Name Error.')

    if correct:
        print('{}, it took you {} guesses to get it right.'.format(username, str(guessNum + 1)))
    else:
        print('{}, I was thinking of {}.'.format(username, str(guessNum + 1), str(randomNum)))



def plus_one():
    while True:
        try:
            number = int(input('{}, please input a number.'.format(username)))
            return print('The answer is: ' + str(number + 1))
        except (ValueError, UnboundLocalError):  # neat that you can code for multiple exceptions
            print('{}, please input a number.'.format(username))


def change_password():
    print("Sorry this isn't functional right now!")
    '''global password
    old_password = input('What is the current password?')
    if old_password == password:
        new_password = input('Please enter a new password. (Note: you only get one chance!)')
        password_file = open("passwords.py", "w")  # opens the file and then writes to it
        password_file.write("password = '{}'".format(new_password))
        password_file.close()
    else:
        print("That's not the password! Intruder detected!!!!")
        sys.exit("You done fucked up")'''


def keystroke_tracker():
    recording = str(keyboard.record(until=chr(27)))
    translation = ''

    i = 0
    while i < len(recording):
        if recording[i:i + 5] == " up),":
            if recording[i - 7:i] == 't(space':
                translation += " "
            elif recording[i - 5:i] == 't(tab':
                translation += "\t"
            elif recording[i - 7:i] == 't(enter':
                translation += '\n'
            elif recording[i - 8:i] == 't(delete':
                translation += ' (delete) '
            elif recording[i - 11:i] == 't(backspace':
                translation += ' (backspace) '
            elif (recording[i - 7:i] == 't(shift' or recording[i - 4:i] == '(alt' or recording[
                                                                                     i - 5:i] == '(ctrl' or recording[
                                                                                                            i - 11:i] == '(right ctrl' or
                  recording[i - 6:i] == 't(down' or recording[i - 4:i] == 't(up' or recording[
                                                                                    i - 7:i] == 't(right' or recording[
                                                                                                             i - 6:i] == 't(left' or
                  recording[i - 12:i] == '(right shift' or recording[i - 11:i] == 't(caps lock' or recording[
                                                                                                   i - 10:i] == '(right alt' or
                  recording[i - 13:i] == '(left windows' or recording[i - 9:i] == 't(windows' or recording[
                                                                                                 i - 6:i] == 't(home' or recording[
                                                                                                                         i - 5:i] == 't(end' or
                  recording[i - 9:i] == 't(page up' or recording[i - 11:i] == 't(page down' or recording[
                                                                                               i - 10:i] == 't(num lock'):
                translation += ""
            else:
                translation += recording[i - 1]
        i += 1

    translation += '\n'
    translation += '\n'
    log = open('keystroke_log.txt', 'a')
    log.write(translation)
    log.close()


username = getpass.getuser()
if not pw.check_user(username):
    password = input("Looks like we have a new user! Please enter a new password...")
    while False:
        pw.add_password(username, password)

for chances in range(6):
    password_guess = getpass.getpass(prompt=f"{username}, what is your password?")  # stream is ignored on windows
    if pw.validate_password(username, password_guess):
        print('You gucci')
        break
    elif chances > 4 and not pw.validate_password(username, password_guess):
        sys.exit()
    else:
        print('You a loser, you got {} chances left'.format(5 - chances))

while True:
    try:
        print('What would you like to do?')
        function_Call = input('You have five options: \n \
                            The plusOne game (enter: plusone) \n \
                            The guessing game (enter: guess it) \n \
                            resetting your password (enter: reset). \n \
                            tracking your keystrokes (enter: tracker). \n \
                            search the web (enter: web) \n \
                            To exit the system, type "exit".')
        if function_Call.lower() == 'plusone':
            plus_one()
        elif function_Call.lower() == 'guess it':
            guessing_game()
        elif function_Call.lower() == 'reset':
            change_password()
        elif function_Call.lower() == 'tracker':
            keystroke_tracker()
        elif function_Call.lower() == 'web':
            websearch()
        elif function_Call.lower() == 'exit':
            break
    except ValueError:
        print('value error')
