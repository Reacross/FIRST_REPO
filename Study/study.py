from math import sqrt, pow
# value_a = float(input("input a "))
# value_b = float(input("input b "))

# value_x = - value_b / value_a
# print(value_x)

# first_cathetus = float(input("enter first cathetus "))
# second_cathetus = float(input("enter second cathetus "))
# area = (first_cathetus * second_cathetus) / 2
# hipotenuse = (first_cathetus ** 2 + second_cathetus ** 2) ** 0.5

# print(f"hipotenuse = {hipotenuse}; area = {area}")

# square_side = float(input('enter square side '))
# print(f"perimeter = {square_side * 4}")
# print(f"perimeter = {float(input('enter square side '))}")    



# value_one = float(input('enter value one : '))
# value_two = float(input('enter value two : '))
# value_three = float(input('enter value three : '))

# absolute_sum = abs(value_one) + abs(value_two) + abs(value_three)

# print(f'{absolute_sum} is the absolute sume of three real numbers')

# print("Result = ", abs(float(input('enter value one : ')))
#                   + abs(float(input('enter value one : ')))
#                   + abs(float(input('enter value one : '))))

# x1_coord = float(input("enter the x coord for the first point: "))
# y1_coord = float(input("enter the y coord for the second point: "))

# x2_coord = float(input("enter the x coord for the first point: "))
# y2_coord = float(input("enter the y coord for the second point: "))

# distance = round(((x2_coord - x1_coord) ** 2 + (y2_coord - y1_coord) ** 2) ** 0.5, 2)

# print("Distance = ", distance)

# # second variant

# print("sqrt((x2-x1)^2 + (y2-y1)^2) = ",
#       round(sqrt(pow(x2_coord - x1_coord, 2) 
#                + pow(y2_coord - y1_coord, 2)), 2))

# Скласти програму, яка вводить із клавіатури чотиризначне число і виводить на екран середнє арифметичне його цифр.
# four_digit_number = int(input("enter four-digit number "))
# thousands = (four_digit_number // 1000) % 10
# print(thousands)
# hundreds = (four_digit_number // 100) % 10
# tens = (four_digit_number // 10) % 10
# units = four_digit_number % 10
# average_sum = (thousands + hundreds + tens + units) / 4
# print(f"average_sum = {average_sum}")


# three_digit_number = int(input("enter three-digit number "))
# hundreds = (three_digit_number // 100) % 10
# tens = (three_digit_number // 10) % 10
# units = three_digit_number % 10

# sum_tens_units = tens + units
# sum_hundreds_units = hundreds + units

# print(f"The sum of the last and penultimate digit = {sum_tens_units}")
# print(f"The sum of the last and first digit = {sum_hundreds_units}")

# three_digit_number = int(input("enter three-digit number "))
# hundreds = (three_digit_number // 100) % 10
# tens = (three_digit_number // 10) % 10
# units = three_digit_number % 10

# result = tens * 100 + hundreds * 10 + units


# print(f"result = {result}")




# Результат пошуку згенерував n записів (вводиться користувачем). Скільки сторінок потрібно для відображення цих записів, якщо на 1 сторінку виводиться 10 записів.

# RECORD_PER_PAGE = 10

# count_of_records = int(input("Enter count of records: "))

# pages_count = (count_of_records - 1) // RECORD_PER_PAGE +1
# print(f"pages is equal to {pages_count}")

# Скласти програму, яка переводить час із секунд, визначаючи повну кількість годин хвилин і секунд (наприклад, час 5000 секунд це 1 година 23 хвилини 20 секунд 5000=1*3600+23*60+20).

# SECOND_IN_HOUR = 3600
# SECOND_IN_MINUTE = 60

# seconds_amount = int(input("Enter amount of seconds: "))

# hours = seconds_amount // SECOND_IN_HOUR
# minutes = (seconds_amount - hours) % SECOND_IN_HOUR // SECOND_IN_MINUTE
# seconds = seconds_amount % SECOND_IN_MINUTE

# print(f" in {seconds_amount}: hours = {hours}, minutes = {minutes}, seconds = {seconds}")

# В Інтернет-магазині зроблено 4 покупки: на $34.34, $12.01, $17.42, $4.93. 
# Зі скількох доларів і центів складатиметься підсумкова сума.


# bill_one = 34.34
# bill_two = 12.01
# bill_three = 17.42
# bill_four = 4.93

# total = bill_one + bill_two + bill_three + bill_four

# dollars = int(total)
# cents = int((total - int(total)) * 100)

# print(f"Total bill = {total}", f"dollars = {dollars}", f"cents = {cents}", sep='\n')

# Скласти програму визначення номера під'їзду та поверху квартири за заданим номером квартири. 
# У будинку 5 поверхів і 4 квартири на поверсі.

# FLOORS = 5
# APARTMENTS_PER_FLOOR = 4

# apartment_number = int(input("Enter apartment number: "))

# apartment_per_entrance = FLOORS * APARTMENTS_PER_FLOOR
# entrance_number = (apartment_number - 1) // apartment_per_entrance + 1
# floor_number = ((apartment_number - 1) % apartment_per_entrance) // APARTMENTS_PER_FLOOR + 1

# print(f"Entrance number = {entrance_number}, Floor number = {floor_number}")

# Скласти програму визначення номера століття с за номером  n(n>0)  деякого року 
# (врахувати що, наприклад, початком 20 століття був 1901, а не 1900 рік).


# current_year = int(input("Enter year: "))

# current_century = (current_year - 1) // 100 + 1

# print(f"Current century is {current_century}")


# Для кава-брейків на конференції закуплено: х круасанів, у стаканчиків, z упаковок кави. 
# Ціна круасана $1.04, ціна стаканчика - $0.34, ціна упаковки кави $4.42. 
# Скласти програму, яка обчислює, скільки повних доларів пішло на закупівлю їжі 
# для кава-брейків, і яка її вартість у доларах і центах.

# PRICE_CROISSANTS = 1.04
# PRICE_CUPS = 0.34
# PRICE_COFFEE = 4.42

# croissants = int(input("Enter croissants: "))
# cups = int(input("Enter cups: "))
# coffee = int(input("Enter coffee: "))



# sum_dollars = croissants * PRICE_CROISSANTS + \
#               cups * PRICE_CUPS + \
#               coffee * PRICE_COFFEE

# only_dollars = int(sum_dollars)
# cents = int(only_dollars * 100)
# print(f'Sum = {sum_dollars}', f'Dollars = {only_dollars}', f'cents = {cents}', sep='\n')  
