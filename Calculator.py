result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        operand = input("Enter the number: ")
        try:
            operand = int(operand)
            wait_for_number = False
            if not operator:
                result = operand
            else:
                if operator == '+':
                    result = result + operand
                elif operator == '-':
                    result = result - operand
                elif operator == '*':
                    result = result * operand
                elif operator == '/':
                    result = result / operand
        except ValueError:
            print(f"{operand} is not a number! Try again.")
    else:
        operator = input("Enter the operator: ")
        if operator in ('+', '-', '*', '/'):
            wait_for_number = True
        elif operator == "=":
            print(result)
            break
        else:
            print(f"{operator} is not '+' or '-' or '*' or '/'")

            



# result = None = False 
# not False = True
# not True = False
        
# = None
# 1-ша ітерація = operand
# += operand

# result = operand
# oprator = +
# result = result + operand
# oprator = *
# result = result * operand
# operator = =
# result = result
# break While.

# 1 + 1 * 2 = 4



# """
# 1число     +
# 2 перевірка числа      +
# збереження числа          +
# (при умові наявності оператора)  дія над числом   +
# збереження результату     +           
# 3 оператор        +
# 4 перевірка оператора   +     
# збереження оператора      +
# поверненння до п. 1
# """

#         SyntaxError — синтаксична помилка.
# IndentationError — помилка, яка виникає, якщо у виділеному блоці інструкцій допущена помилка з пробілами.
# TabError виникає, якщо в одному файлі використовувати пробіли та табуляції для виділення блоків інструкцій.
# TypeError виникає, коли операція зі змінною цього типу неможлива.
# ValueError виникає, коли тип операнда відповідний, але значення таке, що операцію неможливо виконати.
# ZeroDivisionError — ділення на нуль.