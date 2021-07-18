proceed = int(input("Введите выручку: "))
outlay = int(input("Введите издержки фирмы: "))
if proceed > outlay:
    profitability = proceed - outlay
    rent = profitability / proceed
    print(f"Хорощая работа, ваша рентабильность {profitability}")
    worker = int(input("Численность ваших сотрудников: "))
    print(f"{profitability / worker} в расчете на одного рабочего")
elif proceed == outlay:
    print("Не плохо")
else:
    print("Удачи!")