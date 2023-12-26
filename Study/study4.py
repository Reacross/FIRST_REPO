# def codes_of_string(string):
#     codes = dict()
#     for char in string:
#         if char not in codes:
#             codes[char] = ord(char)
#     return codes

# print(codes_of_string('Hello world'))

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
# def main():
#     user_input = int(input('enter natural number: '))
#     if is_prime(user_input):
#         print(f"{user_input} -- is prime number")
#     else:
#         print(f"{user_input} -- is not prime number")


# if __name__ == "__main__":
#     main()

# def to_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):
#     seconds_in_minutes = 60
#     seconds_in_hours = seconds_in_minutes * 60
#     seconds_in_day = seconds_in_hours * 24
#     seconds_in_week = seconds_in_day * 7

#     return seconds +\
#         minutes * seconds_in_minutes +\
#         hours * seconds_in_hours +\
#         days * seconds_in_day +\
#         weeks * seconds_in_week

# print(to_seconds(minutes=56, weeks=2, days=3))

# price_bread = 20
# price_butter = 70
# price_sugar = 40

# def actual_price(item, discount: float = 0):
#     return item * (1 - discount)

# def percent_value(discount=0):
#     return discount * 100

# print(f"Previos price on bread {price_bread}, new price {actual_price(price_bread)} with {percent_value()}% discount")
# print(f"Previos price on butter {price_butter}, new price {actual_price(price_butter, 0.35)} with {percent_value(0.35)}% discount")
# print(f"Previos price on sugar {price_sugar}, new price {actual_price(price_sugar, 0.05)} with {percent_value(0.05)}% discount")


# def max_value_of_funtion(x_start, x_end, step=0.5):
#     a = 2.14
#     b = -4.21
#     c = 3.25

#     max_value = float('-inf')
#     x = x_start
#     while x <= x_end:
#         y = a * pow(x, 3) + b * x - c
#         if y > max_value:
#             max_value = y        
        
#         x += step

#     return max_value


# print(max_value_of_funtion(0, 10))



# def factorial(n):
#     return 1 if n < 2 else n * factorial(n - 1)


# def sum_inf(epsilon = 0.0001):
#     i = 1
#     sum = pow(-1, i) / factorial(i + 1)
    
#     while True:
#         i += 1
#         result = pow(-1, i) / factorial(i + 1)
#         if abs(result) < epsilon:
#             break
#         sum += result
#     return(sum)


# print(sum_inf())

# MASTER_WORK = 75
# HUNDRED_PAPER_PRICE = 120
# INK_PRICE = 20

# def profit(p, n):
#     if n % 100 != 0:
#         return "Error. Not divide by 100"
    

#     hundreds = n // 100
#     return n * p - hundreds * (MASTER_WORK + HUNDRED_PAPER_PRICE + INK_PRICE)

# print(profit(2.15, 10000))


# MASTER_WORK = 75
# HUNDRED_PAPER_PRICE = 120
# INK_PRICE = 20

# TAX_MIN = 0.05
# TAX_MID = 0.08
# TAX_MAX = 0.15

# def profit(p, n):
#     if n % 100 != 0:
#         return "Error. Not divide by 100"
    

#     hundreds = n // 100
#     return n * p - hundreds * (MASTER_WORK + HUNDRED_PAPER_PRICE + INK_PRICE)

# def profit_after_tax(p, n):
#     profit_befor_tax = profit(p, n)
#     if profit_befor_tax < 100_000:
#         return profit_befor_tax * (1 - TAX_MIN)
#     elif profit_befor_tax < 1_000_000:
#         return profit_befor_tax * (1 - TAX_MID)
#     else:
#         return profit_befor_tax * (1 - TAX_MAX)

# print(profit(2.5, 50000))
# print(profit_after_tax(2.5, 50000))

# from random import randint

# def predict_number(number):
#     count = 0
#     goal = randint(0, number)
    
#     while True:
#         user_input = int(input(f"Guess the number from 0 to {number}: "))
#         count += 1

#         if user_input > goal:
#             print("Smaller")
#         elif user_input < goal:
#             print('Larger')
#         else:
#             print(f"You win. Count of try's = {count}")
#             break

# predict_number(8)