#Задание 1: Базовая обработка исключений

#Напиши функцию safe_divide, которая принимает два аргумента: a и b. Функция должна пытаться делить a на b и возвращать результат.
#Если произойдет ошибка деления на ноль (ZeroDivisionError), функция должна возвращать None вместо возникновения исключения.
#Продемонстрируй работу функции на нескольких примерах, включая деление на ноль.


def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
num1 = float(input("Введите числитель (a): "))
num2 = float(input("Введите знаменатель (b): "))
result = safe_divide(num1, num2)


if result is not None:
    print("Результат деления:", result)
else:
    print("Ошибка: деление на ноль.")