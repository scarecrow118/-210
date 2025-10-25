def a_b_func(a, b):
    return a, b

this_is_lambda = lambda first, age: f"Цей код написав: {first}, мені {age:5d} років"

print("Це просто функція:", a_b_func)
print("А це лямбда:", this_is_lambda)
print("\nЇї виклик:", this_is_lambda("Юрій", 19))
print("Передача аргументів через звичайну функцію:", this_is_lambda(*a_b_func("Олег", 30)))

people = [("Іван", 22), ("Марія", 19), ("Олексій", 35)]
sorted_people = sorted(people, key=lambda p: p[1])  # сортування за віком
print("\nСписок людей, відсортований за віком:", sorted_people)
