import time

print("Загрузка... ")
time.sleep(4)
while True:
    a = input("Введите команду: ")
    if a == "Калькулятор":
        calc1 = float(input("Число 1: "))
        calc2 = float(input("Число 2: "))
        calc3 = input("Что сделать (+,-,/,*): ")
        if calc3 == "+":
              answer1 = (calc1 + calc2)
              print(str(answer1))
              print("Это ответ")
        if calc3 == "-":
              answer1 = (calc1 - calc2)
              print(str(answer1))
              print("Это ответ")
        if calc3 == "/":
              answer1 = (calc1 / calc2)
              print(str(answer1))
              print("Это ответ")
        if calc3 == "*":
              answer1 = (calc1 * calc2)
              print(str(answer1))
              print("Это ответ")
    elif a == "Помощь":
        print("команда Помощь - показывает все команды RUSDos")
        print("Команда Калькулятор - решает примеры")
        print("команда Версия - даёт версию RusDos")
    elif a == "Версия":
        print("Версия Demo 0.1.1 ")
