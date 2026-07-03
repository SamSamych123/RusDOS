import time

print("Загрузка... ")
time.sleep(1.16)
print('''   ССССССССССС
  С           С            
 С                          
С                           
С                           
С                           
С                           
С                           
 С                        
  С           С      ...     
   ССССССССССС       ...''')
print('''

Это
все
КОМАНДЫ
в
RusDos


Команда калькулятор - решает примеры
Команда версия - даёт версию RusDos
Команда блокнот - сохраняет то, что вы написали (Внимание! В этой команде когда вы чтото в слот запишете, то это уже не стереть (Если вы не найдёте файл данных в расположении программы))
Комонда чат-бот - это бот, с которым можно разговаривать
Команда игры - можно поиграть в игры (НАКОНЕЦТО!!!!!)


''')
while True:
    a = input("Введите команду): ")
    if a == "калькулятор":
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
    elif a == "версия":
        print("Версия RusDos(Russia Disk Operation System) 4.1: теперь не надо делать заглавную букву к каждой команде, а ещё можно поддержать наш проект по команде 'поддержать проект'")
    elif a == "блокнот":
        b = input("Что вы хотите сделать (прочитать слот(Прочитать) или написать там чтото в дополнение(Дополнить)(На заметку: если вы хотите сделать другую стоку, то НЕ НАЖИМАЙТЕ НА ENTER!). (А чтобы выйти напишите 'Выход'(Совсем выйти)))? Введите решение в поле ввода: ")
        if b == "дополнить":
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
                time.sleep(1)

        elif b == "прочитать":
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
                time.sleep(1)
        elif b == "выход":
            break
    elif a == "чат-бот":
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
                print("К сожалению вы выбрали неправильную команду.")
                time.sleep(1)
    elif a == "игры":
        print("Игра 'симулятор владельца завода'")
        d = input("Введите игру, которую хотите играть: ")
        if d == "симулятор владельца завода":
            dengi = 1000
            product = 10
            corpusov = 2
            popy = 2
            mesta1 = 100
            mesta2 = mesta1 - product
            print('''   ССССССССССС
  С           С            
 С                          
С                           
С                           
С                           
С                           
С                           
 С                        
  С           С      ...     
   ССССССССССС       ...''')
            while True:
                print('У вас ', product, ' штук продукта')
                print('У вас ', corpusov, ' корпуса(ов)')
                print('У вас ', dengi, ' денег')
                print('У вас ', popy, '% популярности')
                print('У вас осталось', mesta2, ' мест в полках из ', mesta1, 'мест')
                deistvie = input("Введите действие(Для помощи введите действие 'Помощь'): ")
                if deistvie == "построить корпус":
                    a1 = dengi - 100
                    a2 = corpusov + 1
                    a3 = product + 40
                    qm = mesta2 - 40
                    dengi = a1
                    corpusov = a2
                    product = a3
                    mesta2 = qm
                elif deistvie == "продать продукт":
                    b1 = dengi + 110
                    b2 = product - 1
                    b3 = mesta2 + 1
                    dengi = b1
                    product = b2
                    mesta2 = b3
                elif deistvie == "создать продукт":
                    c1 = product + 1
                    c2 = dengi - 15
                    c3 = mesta2 - 1
                    product = c1
                    dengi = c2
                    mesta2 = c3
                elif deistvie == "снести корпус":
                    d1 = corpusov - 1
                    d2 = dengi - 8
                    d3 = mesta2 + 40
                    d4 = product - 40
                    product = d4
                    corpusov = d1
                    dengi = d2
                    mesta2 = d3
                elif deistvie == "снести завод":
                    print("Ваш завод снесли, и у вас недостаток денег, чтобы нормально покушать.")
                    print("Game Over")
                    input("")
                    break
                elif deistvie == "благотворительность":
                        print("Сколько вы хотите отдать на благотворительность?")
                        blag = input("Введите сумму (150, 200, 250, 300 денег): ")
                        if blag == "150":
                            print("Всмысле Уитли краб?")
                            qa = popy + 1
                            qb = dengi - 150 + 300
                            popy = qa
                            dengi = qb
                        elif blag == "200":
                            print("Кашка Геркулес и колбаса Папа может лудше чем в двух версиях Портал одну и туже стрелку менять десять раз.")
                            qc = popy + 2
                            qd = dengi - 200 + 350
                            popy = qc
                            dengi = qd
                        elif blag == "250":
                            print("Панды едят кашку Геркулес!!!!!")
                            qe = popy + 3
                            qf = dengi - 250 + 400
                            popy = qe
                            dengy = qf
                        elif blag == "300":
                            print("Ура! Поко теперь не взрываются!")
                            qg = popy + 5
                            qq = dengi - 300 + 450
                            popy = qg
                            dengi = qq
                elif deistvie == "помощь":
                      print('''

Есть действие благотворительность, снести завод(конец игры), снести корпус,
создать продукт, продать продукт, разширить склад и построить корпус.


''')
                elif deistvie == "разширить склад":
                    jh = dengi - 50
                    ji = mesto1 + 25
                    dengi = jh
                    mesto1 = ji
                else:
                    print("Вам выписан штраф 25 денег за незаконные действия. Даже Блоптоп, или Xiaomi не нарушают законы.")
                    print('''      ||||      ||||
      ||||      ||||


    ------------------
  /                    \
 |                      |
        ''')
                    qr = dengi - 25
                    dengi = qr
                if dengi == 0:
                    break
                if mesta2 == mesta1:
                    print("У вас переполнено место.")
                    print("Game Over")
                    input("")
                    break

    elif a == "поддержать проект":
        input("Введите сумму(В рублях): ")
        print("Спасибо что поддержали наш проект! Теперь выход новой версии будет ускорен!!!!!")
    else:
        print("К сожалению вы выбрали неправильную команду.")
