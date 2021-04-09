import os
import getpass

username = getpass.getuser()
print(username)

def plusOne():
    while True:
        try:
            number = int(input('{}, please input a number.'.format(username)))
            return(print('The answer is: ' + str(number + 1)))
        except (ValueError, UnboundLocalError):
            print('{}, please input a number.'.format(username))
            

plusOne(number)
