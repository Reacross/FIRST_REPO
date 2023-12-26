"""

2. Тип - рядок
3. Довжина - 4 символи
4. Тільки цифри
1. Відсутність дублікатів ++
"""

def is_valid_pin_codes(pin_codes):
    option_1 = False
    option_2 = False
    for pin in pin_codes:
        if type(pin) == str and len(pin) == 4:
            try:
                int(pin)
                # print(i)
                option_1 = True
            except ValueError:
                return False
        else:
            return False
    pin_set = set(pin_codes)
    if len(pin_codes) == len(pin_set):
        option_2 = True
        
    return option_1 and option_2


# Варіант 2

def is_valid_pin_codes(pin_codes):
    for i in pin_codes:
        if type(i) == str and len(i) == 4:
            try:
                int(i)
            except ValueError:
                return False
        else:
            return False
        
    pin_set = set(pin_codes)
    if len(pin_codes) != len(pin_set):
        return False
    
    return True

    
print(is_valid_pin_codes(['1101', '9034', '0011', '1234']))
