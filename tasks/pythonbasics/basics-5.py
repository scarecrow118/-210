from random import randint

A = randint(0, 1)
print("1️⃣ Просте розгалуження:")
print(f"Значить A = {A}" if A else "Але може бути, що A = {}".format(A))
print()  

print("2️⃣ Багаторівневе розгалуження:")
number = randint(-5, 5)
if number > 0:
    print(f"Число {number} є додатним.")
elif number < 0:
    print(f"Число {number} є від’ємним.")
else:
    print(f"Число {number} дорівнює нулю.")
print()

print("3️⃣ Вкладене розгалуження:")
age = randint(10, 30)
if age >= 18:
    if age < 21:
        print(f"Вік {age}: дорослий, але ще не досяг 21 року.")
    else:
        print(f"Вік {age}: повнолітній і старше 21.")
else:
    print(f"Вік {age}: неповнолітній.")
