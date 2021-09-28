# *** логические и условные операторы (наконец-то!)

# операторы сравнения - для сравнивания каких-либо значений:

z = 3
w = 2

# операвция "равно"
# мы справшиваем "значение z равно значению w?"
result = z == w

print(result)

# операция "не равно"
result = z != w

print(result)

# операция "меньше"
result = z < w

print(result)

# операция "больше"
result = z > w

print(result)

# операция "меньше либо равно"
result = z <= w

print(result)

# операция "больше либо равно"
result = z >= w

print(result)

# чистые логические операции
# булевы функции пишутся с большой буквы
var_1 = True
var_2 = False

# оператор "НЕ" (NOT, инверсия) - работает с одним операндом
result = not var_2

print(result)

# оператор "И" - (AND, конъюнкция) - возвращает True, если только оба "Тrue"
result = var_1 and var_2

print(result)

# оператор "ИЛИ" - (or, дизъюнкция) - возвращает False, если только оба "False"
result = var_1 or var_2

print(result)

# это все были операции - логические вентили - используется в транзисторах - по такой функции работают процессоры
# они нужны для комбинации логических операторов - можно регулировать поведение ботов. Имеет решенпие при определенных условиях

# пример комбинации логических операторов
a = 5
b = 3
c = 7

result = ((a>b) and (b != c)) or (a == c) #условные деревья - сочетание многих условий 

print(result)