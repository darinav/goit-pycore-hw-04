# Завдання 4

## Опис

Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.
☝ Бот помічник повинен стати для нас прототипом застосунку-асистента, який ми розробимо в наступних домашніх завданнях. Застосунок-асистент в першому наближенні повинен вміти працювати з книгою контактів та календарем.

## Що ми створюємо

У цій домашній роботі зосередимося на інтерфейсі самого бота. Найпростіший і найзручніший на початковому етапі розробки інтерфейс — це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати.

Будь-який CLI складається з трьох основних елементів:

* **Парсер команд** — розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
* **Функції-обробники команд** (*handler*) — безпосереднє виконання команд.
* **Цикл запит-відповідь** — отримання від користувача даних та повернення відповіді від handler-а.

На першому етапі бот повинен:

* зберігати ім’я та номер телефону,
* знаходити номер за ім’ям,
* змінювати наданий номер,
* виводити всі записи.

Для цього використовуємо словник: ключ — ім’я, значення — телефон.

---

## Вимоги до завдання

* Програма повинна мати функцію `main()`, яка управляє основним циклом обробки команд.
* Реалізуйте функцію `parse_input()`, яка розбиратиме введений користувачем рядок на команду та її аргументи.
* Команди та аргументи мають бути розпізнані незалежно від регістру введення.
* Програма повинна обробляти команди користувача через відповідні функції.
* Команди "exit" або "close" повинні завершувати програму.
* Функції-обробники: `add_contact()`, `change_contact()`, `show_phone()`, `show_all()` тощо.
* Словник зберігає імена як ключі, а телефони як значення.
* Невірні команди повинні оброблятись з повідомленням "Invalid command."

---

## Рекомендації для виконання

### Формати команд:

1. **hello**

   * Введення: `hello`
   * Вивід: `How can I help you?`

2. **add \[ім'я] \[номер телефону]**

   * Введення: `add John 1234567890`
   * Вивід: `Contact added.`

3. **change \[ім'я] \[новий номер]**

   * Введення: `change John 0987654321`
   * Вивід: `Contact updated.` або помилка, якщо ім’я не знайдено

4. **phone \[ім'я]**

   * Введення: `phone John`
   * Вивід: номер або помилка

5. **all**

   * Введення: `all`
   * Вивід: всі збережені контакти

6. **close / exit**

   * Вивід: `Good bye!` та завершення роботи

---

## Початковий код

```python
def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
```

### Поведінка

```text
Welcome to the assistant bot!
Enter a command: test
Invalid command.
Enter a command: hello
How can I help you?
Enter a command: exit
Good bye!
```

---

## Парсер команд

```python
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
```

```python
def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
```

> ☝ **Навіщо приводити команду до нижнього регістру?**
> Команди типу `Hello`, `HELLO`, `hello` трактуються однаково. Це спрощує обробку вводу.

---

## Додаємо команду add

```python
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
```

> ❗ Якщо контакт уже існує — буде перезаписаний без попередження.

> ⚠ Якщо `args` не містить 2 елементів — виникне помилка `ValueError`. Обробку помилок можна реалізувати пізніше через декоратори.

---

## Критерії оцінювання

* Нескінченний цикл очікування команд.
* Команди не чутливі до регістру.
* Реалізовані команди:

  * `hello`
  * `add username phone`
  * `change username phone`
  * `phone username`
  * `all`
  * `exit`, `close`
* Логіка реалізована у функціях.
* Вся взаємодія з користувачем (input/print) — лише в `main()`.
