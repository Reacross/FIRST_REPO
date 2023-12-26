#  Коллекції в Пайтон
# Списки


# пустий список
# my_list = []

# my_list = list()

# Заповнений список

# my_list = [5, 18, 32, 25]

# Ітенрація списку

# # for elem in my_list:
# #     print(elem)

# for elem in range(len(my_list)):
#     if my_list[elem] > 20:
#         print(my_list[elem])


# Робота з індексами
# user_one = ['Oleh', 20, 'Ukraine']
# user_two = ['Vova', 22, 'Poland']

# print(user_two[2])
# print(user_one[2])

# user_one = ['Oleh', 20, 'Ukraine']
# user_one_dict = {0: 'Oleh', 1: 20, 2: 'Ukraine'}

# Дії над списками
# my_list = [5, 18, 32, 25]
# # Додати елемент в кінець списка
# my_list.append(16)
# print(my_list)
# # Додати елемент в конкретне місце списку за індексом
# print(my_list[3])

# my_list.insert(3, 12)
# print(my_list)
# # Видалити елемемнт за значенням
# my_list.remove(32)
# print(my_list)
# # Видалити останній елемент
# my_list.pop()
# print(my_list)
# # Видалити елемент за індексом  
# my_list.pop(0)
# print(my_list)
# Розширення елементами іншого списку
# new_list = ["Oleh", 'Petro']

# my_list.extend(new_list)
# print(my_list)

# # Видалення по значенню

# my_list = [5, None, 18, 32, 14, None, 32, 625, 375, None, 25]
# print(my_list)

# for _ in range(len(my_list)):
#     if None not in my_list:
#         break
#     my_list.pop(my_list.index(None))

# print(my_list)

# # Копіювання списків

# my_list = [5, None, 18, 32, 14, None, 32, 625, 375, None, 25]
# new_list = my_list
# new_list.append(6)
# print(new_list, my_list, sep='\n')

# new_list = my_list.copy()
# new_list.append(8)
# print(new_list, my_list, sep='\n')

# # Сортування списків

# my_list = [5, 18, 32, 14, 32, 625, 375, 25]

# sorted_list = sorted(my_list.copy())
# print(my_list)
# print(sorted_list)

# my_list.sort()
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)


# my_list = [5, 18, 32, 14, 32, 625, 375, 25]

# my_list.insert(my_list.index(32), 1000000)
# print(my_list)

# my_list[my_list.index(32)] = 999999
# print(my_list)

# # Заповнення і сортування списку через цикл
# my_list = list()

# user_input = int(input('Enter value: '))
# while user_input != 0:
#     if user_input not in my_list:
#         my_list.append(user_input)
#     user_input = int(input('Enter value: '))

# print(sorted(my_list))
#  Слайси
# my_list = [5, 18, 32, 14, 32, 625, 375, 25]

# print(my_list[::-1])
# print(my_list[-1])
# print(my_list[3:])
# print(my_list[:6])
# print(my_list[2:5])
# print(my_list[:6:-1])
# print(my_list[:])

# # Словники

# person = {'name':'Oleh', 'age':23, 'phone':'+380**********', 'married':False}
# print(person)
# print(person['name'])

# new_data = {'location':'Ukraine', 'lang':'ukr'}
# # Оновлення словника новими даними
# person.update(new_data)
# print(person)
# # Видалення пари ключ-значення по ключу
# person.pop("lang")
# print(person)
# # Зміна значення по ключу
# person['age'] = 100
# print(person)