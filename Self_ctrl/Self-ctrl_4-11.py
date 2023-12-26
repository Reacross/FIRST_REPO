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