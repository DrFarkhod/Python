#3
firm = {'Иванов': 245, 'Петров': 166, 'Сидоров': 145, 'Максимов': 235}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 1
count = 1
persons = []
with open("3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
    if int(tokens[1]) >= 200:
        persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
        result = summa / count
print(f"persons: {persons}")
print(f"averate: {result}")


