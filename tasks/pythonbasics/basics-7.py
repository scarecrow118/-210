try:
    with open("README.md", "r", encoding="utf-8") as f:
        print("Вміст файлу README.md:")
        for i, line in enumerate(f):
            print(f"{i + 1})> {line.strip()}")
except FileNotFoundError:
    print("Файл README.md не знайдено! Створимо новий файл нижче.\n")

text_lines = ["Перша лінія", "Друга лінія", "Третя лінія"]
with open("example.txt", "w", encoding="utf-8") as f:
    for line in text_lines:
        f.write(line + "\n")
print("Файл 'example.txt' створено та записано!\n")

with open("example.txt", "r", encoding="utf-8") as src, open("copy.txt", "w", encoding="utf-8") as dst:
    for line in src:
        dst.write(line.upper())
print("Вміст 'example.txt' скопійовано у 'copy.txt' у верхньому регістрі!")
