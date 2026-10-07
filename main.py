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
