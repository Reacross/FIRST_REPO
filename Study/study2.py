# name = "Alex"


# if name == "Bob" or "Tom" or "Mike":
#     print("Access Granted")
# else:
#     print("Access Denied")

# if name == "Bob" or name == "Tom" or name == "Mike":
#     print("Access Granted")
# else:
#     print("Access Denied")

# entry = input("Enter password: ")

# if entry is 'test2023':
#     print("Access Granted")
# else:
#     print("Access Denied")

# if entry == 'test2023':
#     print("Access Granted")
# else:
#     print("Access Denied")

# print(id(entry))
# print(id('test2023'))


# balance = 0.7 + 0.6
# print(balance)
# if balance >= 1.3:
#     print('Enough')
# else:
#     print("Not enough")


# if round(balance, 1) >= 1.3:
#     print('Enough')
# else:
#     print("Not enough")

# number = int(input("Enter natural number: "))

# result = 'even' if number % 2 == 0 else 'odd'
# print(f"the number is {number} is {result}")

# result = (number % 2 == 0) and 'even' or 'odd'
# print(f"the number is {number} is {result}")

# number = input("Enter natural number: ")
# sum = 0
# for char in number:
#     num = int(char)
#     sum += num

# for digit in number:
#     sum += int(digit)


# string_one = input('enter string: ')
# string_two = input('enter string to compare: ')


# for char in string_one:
#     if char not in string_two:
#         print(False)
#         break
# else:
#     print(True)

# num_one, num_two = 0, 1

# for _ in range(10):
#     print(num_one, end=" ")
#     num_one, num_two = num_two, num_one + num_two


# while True:
#     is_prime = True
#     try:
#         user_input = int(input('Enter number: '))

#         if user_input < 0:
#             break
#         for i in range(2, int(user_input ** 0.5) + 1):
#             if user_input % i == 0:
#                 is_prime = False
#         else:
#             print(is_prime)
#     except ValueError:
#         print("Not natural number!")


# try:
#     user_input = int(input('Enter number: '))
#     for number in range(user_input):
#         if user_input < 0:
#             break
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 break
#         else:
#             if number == 0 or number == 1:
#                 continue
#             print(number)
# except ValueError:
#     print("Not natural number!")

# number = int(input("enter three-digit number: "))

# hunder = number // 100
# units = number % 10

# if hunder == units:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# a = int(input("enter a:"))
# b = int(input("enter b:"))

# if (a >= 1 and a <= 20) and (b >= 1 and b <= 20):
#     sum = 0
#     mul = 1
#     if a > b:
#         a, b = b, a

#     for elem in range(a, b +1):
#         sum += elem
#         mul *= elem

#     print(f"Sum: {sum}, product of numbers: {mul}")
# else:
#     print("The numbers are out of diapazone")

# k = int(input("enter k: "))
# l = int(input("enter l: "))

# if k != l:
#     if k < l:
#         k = l
#     else:
#         l = k


# else:
#     k, l = 0, 0 
# print(f"k is equal {k}, l is equal {l}")



# PERCENT = 0.05

# deposit = 100
# waiting_year = 10

# print(round(deposit * (1 + PERCENT / 12) ** (12*10), 2))
# for year in range(1, waiting_year + 1):
#     new_deposit = deposit * (1 + PERCENT / 12) ** 12
#     deposit = new_deposit

# print(round(deposit, 2))



# string = input('enter string: ')
# string = string.lower()

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")



# string = input('enter string: ')


# count_symbols = 0
# count_a = 0
# count_o = 0
# count_t = 0
# count_space = 0

# for char in string:
#     count_symbols += 1
#     if char == 'a':
#         count_a += 1
#         continue
#     if char == 'o':
#         count_o += 1
#         continue
#     if char == 't':
#         count_t += 1
#         continue
#     if char == ' ':
#         count_space += 1
#         continue

# print(f"Count of symbols 'a' {count_a} - percentage in sentence {round((count_a / count_symbols) * 100, 2)}")
# print(f"Count of symbols 'o' {count_o} - percentage in sentence {round((count_o / count_symbols) * 100, 2)}")
# print(f"Count of symbols 't' {count_t} - percentage in sentence {round((count_t / count_symbols) * 100, 2)}")
# print(f"Count of words {count_space} ")

# from math import sqrt, pow
# triangle_type = None
# side1 = float(input("enter first side of triangle: "))
# side2 = float(input("enter second side of triangle: "))
# side3 = float(input("enter third side of triangle: "))

# if (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
#     if side1 == side2 and side2 == side3 and side1 == side3:
#         triangle_type == 'equilateral'
#     elif side1 == side2 or side2 == side3 or side1 == side3:
#         triangle_type = 'isosceles'
#     elif sqrt(pow(side1, 2) + pow(side2, 2)) == side3 or \
#          sqrt(pow(side2, 2) + pow(side3, 2)) == side1 or \
#          sqrt(pow(side1, 2) + pow(side3, 2)) == side2:
#         triangle_type = 'right-angeled'
#     else:
#         triangle_type = 'differential'
#     print(triangle_type)
# else:
#     print("Not triangle")
         