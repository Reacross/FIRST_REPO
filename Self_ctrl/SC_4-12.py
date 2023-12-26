from random import randint


def get_random_password():
    password = ""
    for i in range(8):
        password += chr(randint(40, 126))              

    return password


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_number = False
    if len(password) == 8:
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isnumeric():
                has_number = True
            else:
                continue
    else:
        return False
    
    return has_upper and has_lower and has_number


def get_password():
    counter = 0
    password = get_random_password()
    while counter < 100:
        if is_valid_password(password):
            break
        password = get_random_password()
        counter += 1
    
    return password