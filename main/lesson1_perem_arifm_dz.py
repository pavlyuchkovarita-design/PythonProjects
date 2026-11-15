#2.1

print()

print("Эта программа считает сколько метров в данном расстоянии(см)")

sm = int(input(f"Введите расстояние в см: "))
m = sm // 100

print(f"Полных метров: {m}")

print()

#2.5

print()

day = 234

week = day // 7
ost_day = day % 7

print(f"Дано 234 дня")
print(f"Полных недель прошло: {week}")
print(f"Оставшихся дней: {ost_day}")

print()

#2.6

print()

n = int(input(f"Введите количество секунд, прошедших с начала суток"))

hours = n // 3600
minutes = n % 3600 // 60
seconds = n % 60

print(f"а) Полных часов прошло: {hours}")
print(f"б) Полных минут прошло с начала часа: {minutes}")
print(f"в) Полных секунд прошло с начала минуты: {seconds}")

print()

#2.7

print()

length = 543
width = 130
side = 130

square_length = length // side
square_width = width // side
sum_square = square_length * square_width

print(f"Можно отрезать: {sum_square} квадратов")

print()