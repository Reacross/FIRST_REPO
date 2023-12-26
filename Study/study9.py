# # Прочитати перші N рядків текстового файлу. Ім'я файлу для читання передаємо як аргумент командного рядка
# import sys

# print(len(sys.argv), sys.argv)

# if len(sys.argv) != 2:
#     print('Not enaugh parameters')
#     quit()

# file = open(sys.argv[1], 'r', encoding="UTF-8")

# try:
#     try:
#         line = file.readline()
#         counter = 0
#         while counter < 0 and line != '':
#             line = line.rstrip()
#             print(line)
#             counter += 1
#             line = file.readline()
#     except OSError:
#         print(f'Error while reading file {sys.argv[1]}')
#     finally:
#         file.close()
# except OSError:
#     print(f"Error with right for file {sys.argv[1]}")

# # Прочитати кінець файлу, останні N рядків файлу. Ім'я файлу для читання передаємо як аргумент командного рядкаi


# import sys

# # print(len(sys.argv), sys.argv)

# if len(sys.argv) != 2:
#     print('Not enaugh parameters')
#     quit()

# NUM_LINES = 10



# try:
#     with open(sys.argv[1], 'r', encoding="UTF-8") as file:
#         lines = list()
#         for line in file:
#             lines.append(line)
#             if len(lines) > NUM_LINES:
#                 lines.pop(0)
#         for line in lines:
#             print(line)

# except Exception as e:
#         print(f'{e} with file {sys.argv[1]}')


# import sys

# # print(len(sys.argv), sys.argv)

# if len(sys.argv) == 1:
#     print('Not enaugh parameters')
#     quit()
# else:
#     print("somesing")

# print(sys.argv)

# for i in range(1, len(sys.argv)):
#     file_name = sys.argv[i]
#     print(file_name)
#     try:
#         with open(sys.argv[1], 'r', encoding="UTF-8") as file:

#             for line in file:
#                 print(line)

#     except Exception as e:
#             print(f'{e} with file {sys.argv[1]}')


# from pathlib import Path

# file_name = Path('./FIRST_REPO')

# try:
#     file = open(file_name/'text.txt', 'r', encoding="UTF-8")
#     try:
#         while True:
#             line = file.readline()
#             line = line.rstrip()
#             if not line:
#                 break
#             print(line)
#     except OSError:
#         print(f'Error while reading file')
#     finally:
#         file.close()
# except OSError:
#     print(f"Error with right for file")

# from pathlib import Path

# file_name = Path('./FIRST_REPO')

# try:
#     with open(file_name/'text.txt', 'r', encoding="UTF-8") as file:
#         for line in file:
#             print(line)
# except Exception as e:
#     print(f'{e} Error while reading file')


# from pathlib import Path

# file_name = Path('.')

# for elem in file_name.glob('*t*'):
#     print(elem)

# for elem in file_name.glob('*.txt'):
#     print(elem)

# for elem in file_name.glob('README*'):
#     print(elem)

# for elem in file_name.glob('*/'):
#     print(elem)

# from pathlib import Path

# try:
#     tmp = Path('text.txt')
#     tmp.unlink()
# except FileNotFoundError:
#     pass

# from pathlib import Path

# new_dir = Path('tmp')

# if not new_dir.exists():
#     new_dir.mkdir()

# new_dir.mkdir(exist_ok=True)


# from pathlib import Path

# new_dir = Path('ABCD/temp/TMP/Exist')

# print(new_dir)

# new_dir.mkdir(parents=True, exist_ok=True)

# from pathlib import Path

# old_dir = Path('main.py')
# new_dir = Path('Self_ctrl/test_main.py')

# old_dir.rename(new_dir)

