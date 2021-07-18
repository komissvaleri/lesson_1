a = float(input("Километраж в первый день: "))
b = float(input("Километраж в последний день: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a / 10
    day += 1
print(day)
