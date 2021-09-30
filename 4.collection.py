# *** коллекции, списки *** 

# список (list)

# создание пустого списка
my_list = []
my_list = list() # класс списка

# создание предварительно наполненного списка
my_list = [10, 20, 3, 7, "python", 3.14] # в [] - включаются элементы, разделенные через запятые

# методы списка - встроенные в объект функции (в самой программе)
# Добавление объекта  (элемента в список)
my_list = []

my_list.append(100)
my_list.append(2.5)
my_list.append("hello")
my_list.append([11, 20, 30])

#print(my_list)

#чтение значений элемента списка
#прямая индексация (слева направо)
el = my_list[0]
el = my_list[3]

#чтение значений
el = my_list[2][1] # 1-й элемент второго элемента

#обратная индексация
el = my_list[-1] # выводит последнюю

#замена значений
my_list[-1] = 777.0 #замена последнего элемента в другую, mutable - изменяемый

#удаление элемента по значению


#print(my_list)
#******************************


my_list = [hello world!]
#срез списка с 3-го индекса до 7-го индекса не включительно
my_slice = my_list[3:7]

#print(my_slice)

#*****************


# длина - параметр, обозначающий число элементов в объекте
print(len(my_list))