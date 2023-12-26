# # Знайти число в параграфі
# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'[0-9]+'

# result = re.search(pattern, string)
# print(result.span())

# first, last = result.span()

# print(string[first:last])

# print(result.group())

# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'[0-9]+'

# result = re.findall(pattern, string)

# print(result)

# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'\d'

# result = re.findall(pattern, string)

# print(result)


# # Пошук за кількістю символів в паттерні
# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'[0-9]{4}' """ в фігурних дужках кількість символів підряд"""

# result = re.findall(pattern, string)

# print(result)


#  Функція Compile


# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'[A-Z]\w+'

# # result = re.findall(pattern, string)
# compiled_pattern = re.compile(pattern)
# # result = compiled_pattern.findall(string)
# result_2 = compiled_pattern.search(string)
# print(result, result_2, sep='\n')

# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'\w+'  '''знаходить і вносить в список всі слова і числа'''

# # result = re.findall(pattern, string)
# compiled_pattern = re.compile(pattern)
# result = compiled_pattern.findall(string)
# print(result)

# # Знайти числа і цифри
# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# def count_digits(string):
#     pattern = r'\d'
#     return re.findall(pattern, string)

# print(count_digits(string))
# print(count_digits(''))


# def count_numbers( string):
#     return re.findall(r'\d+ ', string)


# print(count_numbers(string))
# print(count_numbers(''))

# # Парсимо URL

# import re

# url_query = "kolichestvo-osnovnih-kamer=3630926;producer=huawei;23777=6-6-5;38435=677049"
# url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

# def get_url_parameter(url_query, pattern=r';|&', key_split='='):
#     object_dict = dict()
#     for elem in re.split(pattern, url_query):
#         key, value = elem.split(key_split)
#         object_dict.update({key: value.replace('+', " ")})
#     return object_dict

# print(get_url_parameter(url_query))
# print(get_url_parameter(url_search))

# import re

# lang = "The best language is Java"
# pattern = "Java"

# compilled_pattern = re.compile(pattern)
# lang = compilled_pattern.sub('Python', lang)
# print(re.sub('is', 'are', lang))

# import re

# string = "Exclude from this [string the groups of] characters [located between] brackets [, ]."

# pattern = r'(\s\[.*?\])'

# print(re.findall(pattern, string))

# def clean_up(string):
#     return re.sub(pattern, '', string)

# print(clean_up(string))


# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# print(re.findall(r'^\w+', string))

# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# print(re.findall(r'\w+\.$', string))


# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# print(re.findall(r'[a-zA-Z]+\.', string))


# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# print(re.findall(r'\b[a-zA-Z]{2}', string))


# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'\d{4}-\d{4}'
# print(re.findall(pattern, string))

# pattern = r'\d{4}-(\d{4})'
# print(re.findall(pattern, string))

# pattern = r'(\d{4})-(\d{4})'
# print(re.findall(pattern, string))


# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# def find_years(string):
#     result = list()
#     pattern = r'(\d{4})-(\d{4})'
#     iterator = re.finditer(pattern, string)
#     for match in iterator:
#         result.append(match.group())

#     return result

# print(find_years(string))

# import re

# text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
#        "abc111@test.com.net "

# # Пошук доменних імен
# print(re.findall(r'[\w.]+@(\w+\.)+\w{2,}', text))
# # Пошук адрес і доменних імен
# print(re.findall(r'([\w.]+@(\w+\.)+\w{2,})', text))
# # Пошук адрес
# print(re.findall(r'[\w.]+@(?:\w+\.)+\w{2,}', text))

# def find_years(string):
#     result = list()
#     pattern = r'([\w.]+@(\w+\.)+\w{2,})'
#     iterator = re.finditer(pattern, string)
#     for match in iterator:
#         result.append(match.group())

#     return result

# import re

# text_url = "The main search site in the world is https://www.google.com The main social network for people in the " \
#            "world is https://www.facebook.com But programmers have their own social network http://github.com There " \
#            "they share their code. some url to check https://www..youtube.com/ www.facebook.com https://www.app.facebook.com My site: https://krabaton.info"

# print(re.findall(r'https?:\/\/\w{3}\.?(?:\w+\.)+\w{2,4}', text_url))