import time

print("Загрузка... ")
time.sleep(4.01)
while True:
    a = input("Введите команду(Подсказка: для того чтобы узнать все команды, надо написать команду 'Помощь'): ")
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
        print('''


Команда Помощь - показывает все команды
Команда Калькулятор - решает примеры
Команда Версия - даёт версию RusDos
Команда Блокнот - сохраняет то, что вы написали (Внимание! В этой команде когда вы чтото в слот запишете, то это уже не стереть (Если вы не найдёте файл данных в расположении программы))
Комонда Чат-бот - это бот, с которым можно разговаривать


''')
    elif a == "Версия":
        print("Версия RusDos(Russia Disk Operation System) Demo 2.0 ")
    elif a == "Блокнот":
        b = input("Что вы хотите сделать (прочитать слот(Прочитать) или написать там чтото в дополнение(Дополнить)(На заметку: если вы хотите сделать другую стоку, то НЕ НАЖИМАЙТЕ НА ENTER!). (А чтобы выйти напишите 'Выход'(Совсем выйти)))? Введите решение в поле ввода: ")
        if b == "Дополнить":
            b21 = input("Выберете слот (от 1 до 5): ")
            b31 = input("")
            if b21 == "1":
                test_file = open('c:\\RusDos\\1.txt', 'w')
                test_file.write(b31)
                test_file.close()
            elif b21 == "2":
                test_file = open('c:\\RusDos\\2.txt', 'w')
                test_file.write(b31)
                test_file.close()
            elif b21 == "3":
                test_file = open('c:\\RusDos\\3.txt', 'w')
                test_file.write(b31)
                test_file.close()
            elif b21 == "4":
                test_file = open('c:\\RusDos\\4.txt', 'w')
                test_file.write(b31)
                test_file.close()
            elif b21 == "5":
                test_file = open('c:\\RusDos\\5.txt', 'w')
                test_file.write(b31)
                test_file.close()
            else:
                print("К сожалению вы выбрали неправильный слот к записи. Вам выписан 'Штраф' за неправильное действие. Подождите немного.")
                time.sleep(30)

        elif b == "Прочитать":
            b22 = input("Выберете слот (от 1 до 5): ")
            if b22 == "1":
                test_file = open('c:\\RusDos\\1.txt')
                print(test_file.read())
            elif b22 == "2":
                test_file = open('c:\\RusDos\\2.txt')
                print(test_file.read())
            elif b22 == "3":
                test_file = open('c:\\RusDos\\3.txt')
                print(test_file.read())
            elif b22 == "4":
                test_file = open('c:\\RusDos\\4.txt')
                print(test_file.read())
            elif b22 == "5":
                test_file = open('c:\\RusDos\\5.txt')
                print(test_file.read())
            else:
                print("К сожалению вы выбрали неправильный слот к чтению. Вам выписан 'Штраф' за неправильное действие. Подождите немного.")
                time.sleep(30)
        elif b == "Выход":
            break
    elif a == "Чат-бот":
        while True:
            print("Здравствуйте! Вы сейчас пользуетесь Beta версией чат бота 'Сосиска'.")
            c = input("Введите вопрос в поле ввода: ")
            if c == "Привет":
                print("Здравствуйте! чем могу помочь?")
            elif c == "Как дела?":
                print("Всё хорошо. А у вас?")
            elif c == "Пока":
                print("Досвидание!")
                break
            elif c == "Реши пример":
                calc11 = float(input("Число 1: "))
                calc22 = float(input("Число 2: "))
                calc33 = input("Что сделать (+,-,/,*): ")
                if calc33 == "+":
                    answer1 = (calc11 + calc22)
                    print(str(answer1))
                    print("Это ответ")
                elif calc33 == "-":
                    answer1 = (calc11 - calc22)
                    print(str(answer1))
                    print("Это ответ")
                elif calc33 == "/":
                    answer1 = (calc11 / calc22)
                    print(str(answer1))
                    print("Это ответ")
                elif calc33 == "*":
                    answer1 = (calc11 * calc22)
                    print(str(answer1))
                    print("Это ответ")
            elif c == "Какой у тебя код?":
                print(''' Всё очень просто! Просто установите Python, и скопируйте это:



while True:
    print("Здравствуйте! Вы сейчас пользуетесь Beta версией чат бота 'Сосиска'.")
    c = input("Введите вопрос в поле ввода: ")
    if c == "Привет":
        print("Здравствуйте! чем могу помочь?")
    elif c == "Как дела?":
        print("Всё хорошо. А у вас?")
    elif c == "Пока":
        print("Досвидание!")
        break
    elif c == "Реши пример":
        calc11 = float(input("Число 1: "))
        calc22 = float(input("Число 2: "))
        calc33 = input("Что сделать (+,-,/,*): ")
    if calc33 == "+":
        answer1 = (calc11 + calc22)
        print(str(answer1))
        print("Это ответ")
    elif calc33 == "-":
        answer1 = (calc11 - calc22)
        print(str(answer1))
        print("Это ответ")
    elif calc33 == "/":
        answer1 = (calc11 / calc22)
        print(str(answer1))
        print("Это ответ")
    elif calc33 == "*":
        answer1 = (calc11 * calc22)
        print(str(answer1))
        print("Это ответ")
    elif c == "Какой у тебя код?":
        print('' ' Всё очень просто! Просто установите Python, и скопируйте это:
        И Т. Д.


''')
            else:
                print("К сожалению вы выбрали неправильную команду. Вам выписан 'Штраф' за неправильное действие. Подождите немного.")
                time.sleep(30)
    else:
        print("К сожалению вы выбрали неправильную команду. Вам выписан 'Штраф' за неправильное действие. Подождите немного.")
        time.sleep(30)
