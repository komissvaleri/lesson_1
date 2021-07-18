n = int(input('Введите количество секунд: '))

hours = n // 3600
residue = n % 3600
minutes = residue // 60
seconds = residue % 60

print(f"Время в формате чч:мм:cc {hours}:{minutes}:{seconds}")
