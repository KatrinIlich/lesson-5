#Создание переменной и присвоение значения
my_string = input()
#Количество символов в введенной строке
print(len(my_string))
#Строка в верхнем регистре
print(my_string.upper())
#Строка в нижнем регистре
print(my_string.lower())
#Строка без пробелов
my_string_no_spaces = my_string.replace(" ","")
print(my_string_no_spaces)
#Первый символ строки
print(my_string[0])
#Последний символ строки
print(my_string[-1])