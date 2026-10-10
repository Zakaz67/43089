# Мини-конспект и задачи по Python

# Вывод и ввод
print("DED", 0, 1, sep="")  # Выведет ded01 без пробелов
# \ помогает выводить кавычки внутри строки
print('Second \' line')

# Задача: Проверка на чётность (тернарный оператор)
user_chislo = int(input("Введите число: "))
result = "Чётное" if user_chislo % 2 == 0 else "Нечётное"
print(result)

# Задача: Проверка возраста
user = int(input("Введите возраст: "))
access = "Доступ разрешён" if user >= 18 else "Доступ запрещён"
print(access)


#2 недели ничо не писал , шяс начну ежедневно заполнять все это :)
1. d = input("enter str")
for b in d:
    if b == "a":
        continue
    print(b)

2.correct_login = "admin" 
correct_password = "1234"

correct_login = input("Enter your login: ")
correct_password = input("Enter your password: ")
if correct_login == "admin" and correct_password == "1234":
    print("Access granted")
else:
    print("Access denied")

3. user = int(input("u chislo:"))

user_list = []
i = 0
b = "vedichislo:" 
while user > i:
    i += 1 
    user_list.append(int(input(b)))

print(user_list)
print("макс числоб", max(user_list))
print("мин число", min(user_list))
print("количество", len(user_list))
user_list.remove(min(user_list))
user_list.remove(max(user_list))

print("Итоговый список:", user_list)

4.tamoma_cross = []

d = "Введите оценку (от 1 до 5) или 'stop' для завершения: "

while True:
    oguri = input(d)
    
    if oguri.lower() == "stop":
        break
    
    val = int(oguri)
    
    if 1 <= val <= 5:
        tamoma_cross.append(val)
    else:
        print("некорректная оценк")

if len(tamoma_cross) == 0:  # или if not tamoma_cross:
    print("Список оценок пуст!")
else:
    len(tamoma_cross)
print(tamoma_cross.count(5))
min(tamoma_cross)
max(tamoma_cross)
tamoma_cross.reverse()
print(tamoma_cross)

5. text = "PythonProgramming"

print(text[:6])     # Первые 6 символов
print(text[-7:])    # Последние 7 символов
print(text[::-1])   # Строка наоборот
print(text[::2])    # Каждый второй символ
print(text[2:-2])   # Без первых и последних 2 символов
print(text[:-5:-1]) # Последние 4 символа в обратном порядке


# Зачем я делаю задания с for?
# Потому что я пока плохо знаю эту тему и мне приходится изучать её заново:
# раньше я относился к учёбе несерьёзно. Теперь буду писать код самостоятельно,
# без жирных подсказок от ИИ :3

# 6. Условие: вывести числа от 1 до 10 включительно с помощью for и range().
for i in range(1, 11):
    print(i)

# 7. Условие: вывести чётные числа от 2 до 30 включительно с помощью for и range().
for i in range(2, 31, 2):
    print(i)

# 8. Условие: перебрать список и найти сумму всех чисел, не используя sum().
# Мой код:
numbers = [14, 7, 23, 5, 18, 42, 9]
sa = 0
for i in numbers:
    sa = sa + i
print(sa)
# Примечание: в задании также нужно было вывести каждый элемент списка.

# 9. Условие: вывести каждый символ строки и посчитать количество букв "m".
# Моя текущая попытка: счётчик работает, но выводятся только найденные буквы "m".
text = "programming"
sa = 0
for i in text:
    if i == "m":
        sa = sa + 1
        print(i)
print(sa)
# TODO: вывести каждый символ строки, а не только букву "m".
