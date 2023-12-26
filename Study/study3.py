# def foo():
#     value_a = 4
#     value_b = 8
#     return value_a + value_b

# print(foo())

# sum_value = foo()
# print(sum_value)


# def add(value_one: int, value_two: int):
#     """
#     function of adding two numbers
    
#     Inpit:
#     value_one = integer
#     value_two = integer

#     Output:
#     :return -> integer
#     """
#     sum_of_two_numbers = value_one + value_two
#     return sum_of_two_numbers

# result: int = add(2, 4)
# print(result)



# def multiply(number_one, number_two, number_three=None):
#     if number_three is None:
#         return number_one * number_two
#     else:
#         return number_one * number_two * number_three
    
# print(multiply(7, 8))
# print(multiply(2, 4, 5))



# def add(number_one, number_two):
#     return number_one + number_two

# print(add(2, 3))

# def sum_of_all_numbers(*nums):
#     sum = 0
#     for value in nums:
#         sum += value
#         return sum

# print(sum_of_all_numbers(2, 3, 4, 5, 6, 'test', None, True, 12))


# def sum_of_all_numbers(*nums):
#     sum = 0
#     print(type(nums))
#     for number in nums:
#         try:
#             sum += float(number)
#         except ValueError:
#             continue
#         except TypeError:
#             continue
#     return sum

# print(sum_of_all_numbers(2, 3, 4, 5, 6, 'test', None, True, 12))


# def greeting(**kwargs):
#     print(kwargs)
#     name = kwargs.get("name")
#     age = kwargs.get("age")
#     print(f"Hello {name}, you are have {age} years old")

# print(greeting(name="Oleg", age="100"))


# def greeting(**kwargs):
#     print(kwargs)
#     name = kwargs.get("name")
#     age = kwargs.get("age", 18)
#     return (f"Hello {name}, you are have {age} years old")

# print(greeting(name="Oleg"))



# def result(value, *transport, **text):
#     print(value)
#     print(transport)
#     print(text)
#     print(text['may']/9)



# print(result(278, 246, 'qwerty', 'adfsgfshgdjhmtr', 2362346, hello="Python", may=45))



# def foo():
#     a = 4
#     b = 8
#     print(f"a = {a}, b = {b}")
#     return a + b

# result = foo()
# print(result)


# x = 10
# def foo(x):
#     print(x)
#     x = 5
#     print(x)

# foo(x)
# print(x)

# password = 1234

# def security(passwd):

#     def divide():
#         nonlocal passwd
#         print(passwd)
#         return passwd / 2
    
#     return divide()


# print(security(password))

# def fibonacci(number):
#     return number if number == 1 or number == 0 else fibonacci(number - 2) + fibonacci(number - 1)
# print(fibonacci(9))


# def factorial(number):
#     if number == 0 or number == 1:
#         return number
#     else:
#         return number * factorial(number - 1)
    
# print(factorial(5))

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * power(base, exponent - 1)
    
# print(power(2, 8))
# print(pow(2, 8))


# def result(*args):
#     print(args)
#     print(args[1:3])

# print(result(78, 346346, 'qwerty', 'password', True))

# print('qwerty'[1:4])

# def is_palindrome(word):
#     print(word)
#     if len(word) <= 1:
#         return True
#     elif word[0] != word[-1]:
#         return False
#     else:
#         return is_palindrome(word[1:-1])
    
# def is_palindor():
#     return word == word[::-1]


# print(is_palindrome('qwertytrewq'))


# import math


# print(math.pi)
# # Найгірний варіант імпорту, бо можливий конфлікт бібілотек
# from math import *

# print(sqrt(4))

# from math import pi


# print(pi)

# from math import pi as PI

# def char_counter(user_input):
#     operator_dict = dict()
#     for char in user_input:
#         if char not in operator_dict.keys():
#             operator_dict[char] = 1
#         else:
#             operator_dict[char] += 1
#         return operator_dict

# user_input = input('enter sentence: ')
# print(char_counter(user_input))
# print(char_counter(user_input).keys())
# print(char_counter(user_input).values())