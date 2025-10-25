print("1️⃣ Цикл for з range():")
for i in range(5):
    print(f"Ітерація номер {i}")
else:
    print("Цикл for завершено!\n")

print("2️⃣ Цикл while:")
count = 0
while count < 3:
    print(f"Значення count: {count}")
    count += 1
else:
    print("Цикл while завершено!\n")

print("3️⃣ Цикл for для списку:")
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Ця конструкція безглузда, але працює!\n")
