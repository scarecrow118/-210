A = 0
try:
    print("Що буде, якщо поділити 10 на", A, "?")
    print(10 / A)
except Exception as e:
    print("Невже це помилка >", e)
finally:
    print("Оце так! Код у finally виконується завжди.\n")

try:
    value = int("Привіт")
    print("Перетворене значення:", value)
except ValueError as e:
    print("Помилка перетворення >", e)
finally:
    print("Блок finally виконано.\n")

try:
    lst = [1, 2, 3]
    print("Четвертий елемент списку:", lst[3])
except IndexError as e:
    print("Помилка індекса >", e)
finally:
    print("Цей блок виконається навіть при помилці!\n")
