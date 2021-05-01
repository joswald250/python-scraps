import random
import re
import string


def generate_password(num=15, punctuation=True):
    word = ""
    i = 0
    for i in range(0, num):
        if punctuation is False:
            temp = random.choice([1, 3])
        else:
            temp = random.choice([1, 2, 3])
        if temp == 1:
            word += random.choice(string.ascii_letters)
        elif temp == 2:
            word += random.choice(string.punctuation)
        else:
            word += random.choice(string.digits)
    if punctuation is False:
        test = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])")
    else:
        test = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_=+`~?><\"';:])")
    while not re.search(test, word):
        word = generate_password(num, punctuation)
    return word


password = generate_password()
