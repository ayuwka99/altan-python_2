# условные операторы

var = 10

# оператор IF

# отступ - внутренность тела - конструкция условного оператора
# отступ имеет синтаксическую силу - нужно обз соблюдать 

# if var != 0:
#     print ("Hello!")

# if False:
#     print("Hi!")

# if  not var<12:
#     print("Hello!")

# оператор ELSE
# var = -1
# if var > 0:
#     print("больше нуля")
# else:
#     print("не больше нуля")

# оператор ELIF = else if
var = 0
if var >0:
    print("больше нуля")
elif var > 0:
    print("меньше нуля")
else:
    print("равно нулю")

# var = "A"

# if var == "A":
#     res = "literal A"   #маленькая и большая буквы - это другие символы
# elif var == "a":    #elif - доподнительное условие 
#     res = "literal a"
# elif var == "C":
#     res = "literal C"

# # print(res)

# # условные операторы - перекрестки в мире программирования

# # боевой пример:
# # сделаем консульный калькулятор:
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))

# op = input("Введите символ операции: ")

# if op == "+":
#     res = num_1 + num_2
# elif op == "-":
#     res = num_1 - num_2
# elif op == "*":
#     res = num_1 * num_2
# elif op == "/":
#     res = num_1 / num_2
# else:
#     res = "Символ операции некорректен :("

# print(f"Результат = {res}")