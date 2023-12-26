# #  Лінія найкращої відповідності

# def best_fit_line(data):
#     list_x = list()
#     list_y = list()

#     for coord in data:
#         list_x.append(coord[0])
#         list_y.append(coord[1])

#     m1 = 0.0

#     for i in range(len(data)):
#         m1 += list_x[i] * list_y[i]

#     m2 = (sum(list_x) * sum(list_y) / len(data))

#     m3 = 0.0

#     for i in range(len(data)):
#         m3 += pow(list_x[i], 2)
    
#     m4 = pow(sum(list_x), 2) / len(data)

#     m = round((m1 - m2) / (m3 - m4), 2)

#     b = round((sum(list_y)/len(list_y)) - m * (sum(list_x)/len(list_x)) , 2)

#     return m, b


# data = list()
# x = input("enter x coord: ")

# while x != "":
#     y = input("enter y coord: ")
#     data.extend([[float(x), float(y)]])
#     x = input("enter x coord: ")

# m, b = best_fit_line(data)

# print(f'y = {m}x + {b}')

# from random import randrange


# def create_deck():
#     suits = ['s', 'h', 'd', 'c']
#     values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

#     deck = list()

#     for suit in suits:
#         for value in values:
#             deck.append(f'{value}{suit}')
#     return deck


# # print(create_deck())


# def shuffle_deck(deck):
#     new_deck = deck.copy()
#     for i in range(0, len(deck)):
#         other_index = randrange(0, len(new_deck))
#         new_deck[i], new_deck[other_index] = new_deck[other_index], new_deck[i]
#     return new_deck


# # print(shuffle_deck(create_deck()))

# def deal(players, cards, deck):
#     if players * cards > len(deck):
#         return deck
    
#     table = list()

#     for _ in range(0, cards):
#         for player in range(players):
#             if player >= len(table):
#                 table.append([deck.pop()])
#             else:
#                 table[player].append(deck.pop())
    
#     return table


# # print(deal(4, 6, shuffle_deck(create_deck())))


# def main(players, cards):
#     init_deck = create_deck()
#     print(f"Open new deck: {init_deck}")

#     deck = shuffle_deck(init_deck)
#     print(f"Shuffle deck: {deck}")

#     print(f"Invite {players} players to table")
#     print(f"giv {cards} cards to each player")

#     table = deal(players, cards, deck)

#     for i in range(players):
#         print(f"player №{i + 1} has cardds{table[i]}")

#     print(f"Deck in the final: {deck}")

# if __name__ == '__main__':
#     main(4, 6)

# Конвертація в азбуку Морзе

# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
#               'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
#               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
#               '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


# def convert_to_morze(text):
#     text = text.upper()
#     result = ""

#     for char in text:
#         if char in morze_dict:
#             result += morze_dict.get(char) + " "
#     return result

# def convert_to_morze(text):
#     text = text.upper()
#     result = list()

#     for char in text:
#         if char in morze_dict:
#             result.append(morze_dict.get(char))
#     return " ".join(result)

# text = input("Enter text:")
# print(convert_to_morze(text))


import sys
from pathlib import Path
folder_path = Path(sys.argv[1])

def parse_folder(path):
    for elements in path.interdir():
        if elements.is_dir():
            print(f"parse folder: this is folder")