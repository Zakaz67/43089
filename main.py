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
