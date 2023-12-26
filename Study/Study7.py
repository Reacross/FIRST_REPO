# numbers = ["123", "456", "321", "10", "75", "abc", "23c"]

# for num in numbers:
#     print(num, num.isdigit())


# articles_dict = [
#     {
#         "playset": "Semi final voleyball strike",
#         "command": "Super Star",
#         "year": 1989,
#     },
#     {
#         "playset": "Quater final Finansial competition",
#         "command": "Actual price",
#         "year": 2020,
#     },
#     {
#         "playset": "Glory speed test call centre of East Erope",
#         "command": "Modern Operators",
#         "year": 1921,
#     },
#     {
#         "playset": "Endless war From Age of Dragons",
#         "command": "Kings of Glory",
#         "year": 2012,
#     }
# ]


# def find_states(key_word, letter_case=False):
#     actual_states = list()

#     if letter_case:
#         for i in range(len(articles_dict)):
#             if articles_dict[i]["playset"].find(key_word) != -1 or \
#                 articles_dict[i]["command"].find(key_word) != -1:
#                 actual_states.append(articles_dict[i])
#     else:
#         for i in range(len(articles_dict)):
#             if (articles_dict[i]["playset"].lower()).find(key_word) != -1 or \
#                 (articles_dict[i]["command"].lower()).find(key_word) != -1:
#                 actual_states.append(articles_dict[i])
#     return actual_states

# print(find_states("Age", False))

# print("Endless war From Age of Dragons".find('Ages'))


# text = """
# This is a sample paragraph. It contains some words, like sample, paragraph, and words.
# Let's count the frequency of each word in this paragraph!
# """

# def find_stop_words(text, stop_word, is_space=False):
#     if is_space:
#         new_text = text.split(' ')
#         for word in new_text:
#             word = word.replace(',', '').replace('.', '').replace('!', '').replace('\n', '')
#             if stop_word.lower() in word.lower() and len(stop_word) == len(word):
#                 return True
#     else:
#         if stop_word.lower() in text.lower():
#             return True
        
#     return False

# print(find_stop_words(text, 'frequency', is_space=True))


# phone_storage = ["380669640547", "0637306465    ", " 420961935171", "632643973", "050832520 ", "38066964O547",
#                  "00000000000", "480730283918", "597632643973", "0986223575", "37(029)7947963",
#                  "+42(050)123-32-34", "38986223575","38(950)123 32 34", "38(050)123 32 3b"]

# codes_operators = {"067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093", "029"}

# # 38 - UA, 42 - IT,  37 - UK 48 - PL

# def clean_up_phone(phone):
    # return (phone.strip()
    #         .removeprefix('+')
    #         .replace('(', '')
    #         .replace(')', '')
    #         .replace('-', '')
    #         .replace(' ', ''))

# def is_valid_phone(phone):
#     if phone.isdigit():
#         if len(phone) == 12:
#             if phone[2] == '0':
#                 return phone[2:5] in codes_operators
#             return False
#         if len(phone) == 10:
#             return phone[:3] in codes_operators
#     return False


# def phone_by_country(list_of_phones):
#     phone_by_country_dict = dict()
#     for i in range(len(list_of_phones)):
#         phone = clean_up_phone(list_of_phones[i])
#         if phone.startswith('38'):
#             phone_by_country_dict.setdefault('UA', []).append(phone)
#         elif phone.startswith('42'):
#             phone_by_country_dict.setdefault('IT', []).append(phone)
#         elif phone.startswith('37'):
#             phone_by_country_dict.setdefault('UK', []).append(phone)
#         elif phone.startswith('42'):
#             phone_by_country_dict.setdefault('PL', []).append(phone)
#         else:
#             phone_by_country_dict.setdefault('UNDEFINED', []).append(phone)

#     return phone_by_country_dict
        

# print(phone_by_country(phone_storage))

# def passed_controls():
#     for phone in phone_storage:
#         phone = clean_up_phone(phone)
#         is_valid = is_valid_phone(phone)
#         if is_valid:
#             print('Phone {:^4}| {:>20}| {:^4} valid'.format(" ", phone, " "*4))
#         else:
#             print('Phone {:^4}| {:>20}| {:^4} invalid'.format(" ", phone, " "*4))


# print(passed_controls())

# pay_system = {
#     5: "MasterCard",
#     4: "Visa",
#     3: "American Express"
# }

# card_number = ["5375414112345678", "2346236356566475", "4168757587879876", "216875758787987d", "3345345O45879876"]

# for card in card_number:
#     print("Payment system {:<20} Is card valid {:6}".format(pay_system.get(int(card[0]), 'UNKNOWN'),
#                                                             str(card.isdigit() and len(card) == 16)))


# map = {ord('з'): 'z',  ord('ю'): 'u'}

# translated = 'зюзю'.translate(map)
# print(translated)

# print(ord('з'))

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]


# MAP = {}

# for key, value in zip(symbols, code):
#     MAP[ord(key)] = value
#     MAP[ord(key.lower())] = value.lower()

# print(MAP)

# result = '34 DE 5C b0'.translate(MAP)

# print(result)

# import re
# from collections import defaultdict

# paragraph = """
# This is a sample paragraph. It contains some words, like sample, paragraph, and words.
# Let's count the frequency of each word in this paragraph!
# """


# def words_frequency_counter(paragraph):
#     pattern = r'\b\w+\b'
#     words = re.findall(pattern, paragraph.lower())
#     words_frequency = defaultdict(int)

#     for word in words:
#         words_frequency[word] += 1

#     return words_frequency

# print(words_frequency_counter(paragraph))