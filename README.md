# goit-algo-hw-03
## Завдання 1:

Парсинг аргументів. Скрипт приймає два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).
Рекурсивне читання директорій:
Написана функція, яка приймає шлях до директорії як аргумент.
Функція перебирає всі елементи у директорії.
Якщо елемент є директорією, функція викликає саму себе рекурсивно для цієї директорії.
Якщо елемент є файлом, він є обробленим для копіювання.
Копіювання файлів:
Для кожного типу файлів створюється новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
Файл з відповідним типом копіюється у відповідну піддиректорію.
Обробка винятків: код правильно обробляє винятки, наприклад, помилки доступу до файлів або директорій.
Після виконання програми всі файли у вихідній директорії рекурсивно скопійовано в нову директорію та розсортовано в піддиректорії за їх розширенням.

##Завдання 2:

Код виконується. Програма візуалізує фрактал «сніжинка Коха».
Користувач має можливість вказати рівень рекурсії.