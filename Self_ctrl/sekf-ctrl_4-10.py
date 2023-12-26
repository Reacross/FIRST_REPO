"""
1. Має бути 8 символів з набору нижче
2. ()*+,-./0123456789:;<=>?
@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
3 діапазон кодування - 40 - 126 в ASCII
"""




from random import randint


def get_random_password():
    password = ""
    for i in range(8):
        password += chr(randint(40, 126))              

    return password


print(get_random_password())

y = "".join([chr(randint(40, 126)) for x in range(8)])
print(y)