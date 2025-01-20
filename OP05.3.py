# Задание 3: Обработка исключений прошлых программ

# Возьми одну из программ, которую мы писали на прошлых уроках, продумай,
# какие ошибки в программе могут появляться(можно прям специально пробовать ее ломать)
# и дополни код конструкцией try-except для обработки выявленных исключений.

def bank(a, years):
    total_amount = a
    interest_rate = 0.10

    for year in range(years):
        total_amount += total_amount * interest_rate

    return total_amount

while True:
    try:
        initial_deposit = float(input("Введите сумму вклада (в рублях): "))
        investment_years = int(input("Введите срок вклада (в годах): "))

        if initial_deposit < 0 or investment_years < 0:
            raise ValueError("Сумма вклада и срок должны быть неотрицательными.")

        final_amount = bank(initial_deposit, investment_years)
        income = final_amount - initial_deposit

        print("Ваш доход по депозиту за", investment_years, "лет составит:", round(income, 2), "рублей.")
        print("Сумма на счету через", investment_years, "лет составит:", round(final_amount, 2), "рублей.")
        break

    except ValueError as e:
        print("Ошибка ввода:", e)
    except Exception as e:
        print("Произошла ошибка:", e)