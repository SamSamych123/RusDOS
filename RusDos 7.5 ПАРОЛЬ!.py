import pickle
import time

print("Загрузка... ")
time.sleep(3.25)
x1 = input("Напишите, какой у вас язык(Русский(Write what your language is(English(输入您要选择的语言(中国人))))): ")
if x1 == "Русский":
    passworld = open('passworld.dat', 'rb')
    password = pickle.load(passworld)
    a = input("Напишите пароль: ")
    if a == password:
        passworld.close()
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


Команда калькулятор - решает примеры
Команда версия - даёт версию RusDos
Команда блокнот - сохраняет то, что вы написали (Внимание! В этой команде когда вы чтото в слот запишете, то это уже не стереть (Если вы не найдёте файл данных в расположении программы))
Комонда чат-бот - это бот, с которым можно разговаривать
Команда игры - можно поиграть в игры
Команда время - показывает время в вашу секунду с точностью
Команда открыть программу №1 - может открыть ЛЮБУЮ программу в Windows (системную (другие просто неработают(которые вы установили(Программу))))


''')
        while True:
            a = input("Введите команду: ")
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
                print("Версия RusDos (Russia Disk Operation System) 7.4")
            elif a == "блокнот":
                b = input("Что вы хотите сделать (прочитать слот(прочитать) или написать там чтото в дополнение(написать)(На заметку: если вы хотите сделать другую стоку, то НЕ НАЖИМАЙТЕ НА ENTER!). (А чтобы выйти напишите 'выход'(Совсем выйти)))? Введите решение в поле ввода: ")
                if b == "написать":
                    b21 = input("Выберете слот (от 1 до 10): ")
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
                    elif b21 == "6":
                        test_file = open('c:\\RusDos\\6.txt', 'w')
                        test_file.write(b31)
                        test_file.close()
                    elif b21 == "7":
                        test_file = open('c:\\RusDos\\7.txt', 'w')
                        test_file.write(b31)
                        test_file.close()
                    elif b21 == "8":
                        test_file = open('c:\\RusDos\\8.txt', 'w')
                        test_file.write(b31)
                        test_file.close()
                    elif b21 == "9":
                        test_file = open('c:\\RusDos\\9.txt', 'w')
                        test_file.write(b31)
                        test_file.close()
                    elif b21 == "10":
                        test_file = open('c:\\RusDos\\10.txt', 'w')
                        test_file.write(b31)
                        test_file.close()
                    else:
                        print("К сожалению вы выбрали неправильный слот к записи.")
                elif b == "прочитать":
                    b22 = input("Выберете слот (от 1 до 10): ")
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
                    elif b22 == "6":
                        test_file = open('c:\\RusDos\\6.txt')
                        print(test_file.read())
                    elif b22 == "7":
                        test_file = open('c:\\RusDos\\7.txt')
                        print(test_file.read())
                    elif b22 == "8":
                        test_file = open('c:\\RusDos\\8.txt')
                        print(test_file.read())
                    elif b22 == "9":
                        test_file = open('c:\\RusDos\\9.txt')
                        print(test_file.read())
                    elif b22 == "10":
                        test_file = open('c:\\RusDos\\10.txt')
                        print(test_file.read())
                    else:
                        print("К сожалению вы выбрали неправильный слот к чтению.")
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
                    elif c == "У меня всё хорошо":
                        print("Отлично!")
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
        

''')
                    else:
                        print("К сожалению вы выбрали неправильную команду.")
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
                    mesta3 = 0
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
                        if mesta2 < mesta3:
                            print("У вас переполнено место.")
                            print("Game Over")
                            input("")
                            break
            elif a == "время":
                o = time.localtime()
                ya = o[0]
                yb = o[1]
                yc = o[2]
                yd = o[3]
                ye = o[4]
                yg = o[5]
                print("Сейчас ", ya, "год, ", yb, "месяц", yc, "день, ", yd, "час(ов), ", ye, "минут и ", yg, "секунд.")
            elif a == "открыть программу":
                import os
                bb = input("Введите программу которую вы хотите запустить: ")
                print('''
        

Можно открыть такие программы как:
        
калькулятор Windows;
проводник Windows;
python;
блокнот Windows;
панель управления Windows;
диспечер устройств Windows;
проигрыватель Windows Media;
средство диагностики DirectX Windows;
диспечер задач Windows.
панель управления процессором


''')
                if bb == "калькулятор Windows":
                      os.system("calc")
                elif bb == "проводник Windows":
                    os.system("explorer")
                elif bb == "python":
                    os.system("python")
                elif bb == "блокнот Windows":
                    os.system("notepad")
                elif bb == "командная строка Windows":
                    os.system("cmd")
                elif bb == "панель управления Windows":
                    os.system("control")
                elif bb == "диспечер устройств Windows":
                    os.system("devmgmt")
                elif bb == "проигрыватель Windows Media":
                    os.system("dvdplay")
                elif bb == "средство диагностики DirectX Windows":
                    os.system("dxdiag")
                elif bb == "диспечер задач Windows":
                    os.system("LaunchTM")
                elif bb == "панель управления процессором":
                    os.system("GfxUI")
                else:
                    print("Вы выбрали программу, которую нельзя открыть.")
            else:
                print("К сожалению вы выбрали неправильную команду.")
        else:
            print("Вы ввели неправильный пароль")
elif x1 == "English":
     print(''' SSSSSSSSSSS
  SS
 SS
SS
SS
SS
SS
SS
  SS
   SS
    SSSSSSSSSSS''')
     print('''


Calculator command - solves examples
Version command - gives the RusDos version
Notepad command - saves what you wrote (Attention! In this command, once you write something into a slot, it cannot be erased (If you do not find the data file in the program location))
Komonda chatbot is a bot that you can talk to
Game Team - you can play games
Time command - shows the time in your second with precision
Command to open program No. 1 - can open ANY program in Windows (system (others simply do not work (that you installed (Program))))


''')
     while True:
         a = input("Enter the command: ")
         if a == "calculator":
             calc1 = float(input("Number 1: "))
             calc2 = float(input("Number 2: "))
             calc3 = input("What to do (+,-,/,*): ")
             if calc3 == "+":
                 answer1 = (calc1 + calc2)
                 print(str(answer1))
                 print("This is the answer")
             if calc3 == "-":
                 answer1 = (calc1 - calc2)
                 print(str(answer1))
                 print("This is the answer")
             if calc3 == "/":
                 answer1 = (calc1 / calc2)
                 print(str(answer1))
                 print("This is the answer")
             if calc3 == "*":
                 answer1 = (calc1 * calc2)
                 print(str(answer1))
                 print("This is the answer")
         elif a == "version":
             print("Version RusDos (Russia Disk Operation System) 7.4")
         elif a == "notepad":
             b = input("What do you want to do (read the slot(read) or write something in addition there(write)(Note: if you want to make another line, then DO NOT PRESS ENTER!). (And to exit write 'exit '(Exit completely)))? Enter the solution in the input field: ")
             if b == "write":
                 b21 = input("Select slot (from 1 to 5): ")
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
                 elif b21 == "6":
                    test_file = open('c:\\RusDos\\6.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 elif b21 == "7":
                    test_file = open('c:\\RusDos\\7.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 elif b21 == "8":
                    test_file = open('c:\\RusDos\\8.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 elif b21 == "9":
                    test_file = open('c:\\RusDos\\9.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 elif b21 == "10":
                    test_file = open('c:\\RusDos\\10.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 else:
                     print("Sorry, you have selected the wrong recording slot.")
             elif b == "read":
                 b22 = input("Select slot (from 1 to 5): ")
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
                 elif b22 == "6":
                    test_file = open('c:\\RusDos\\6.txt')
                    print(test_file.read())
                 elif b22 == "7":
                    test_file = open('c:\\RusDos\\7.txt')
                    print(test_file.read())
                 elif b22 == "8":
                    test_file = open('c:\\RusDos\\8.txt')
                    print(test_file.read())
                 elif b22 == "9":
                    test_file = open('c:\\RusDos\\9.txt')
                    print(test_file.read())
                 elif b22 == "10":
                    test_file = open('c:\\RusDos\\10.txt')
                    print(test_file.read())
                 else:
                     print("Sorry, you have selected the wrong reading slot.")
             elif b == "exit":
                 break
         elif a == "chatbot":
             while True:
                 print("Hello! You are currently using the Beta version of the 'Sausage' chat bot.")
                 c = input("Enter a question in the input field: ")
                 if c == "Hello":
                     print("Hello! How can I help you?")
                 elif c == "How are you?":
                     print("Everything is fine. How about you?")
                 elif c == "I'm fine":
                     print("Great!")
                 elif c == "Bye":
                     print("Goodbye!")
                     break
                 elif c == "Solve the example":
                     calc11 = float(input("Number 1: "))
                     calc22 = float(input("Number 2: "))
                     calc33 = input("What to do (+,-,/,*): ")
                     if calc33 == "+":
                         answer1 = (calc11 + calc22)
                         print(str(answer1))
                         print("This is the answer")
                     elif calc33 == "-":
                         answer1 = (calc11 - calc22)
                         print(str(answer1))
                         print("This is the answer")
                     elif calc33 == "/":
                         answer1 = (calc11 / calc22)
                         print(str(answer1))
                         print("This is the answer")
                     elif calc33 == "*":
                         answer1 = (calc11 * calc22)
                         print(str(answer1))
                         print("This is the answer")
                 elif c == "What's your code?":
                     print(''' It's very simple! Just install Python, and copy this:



while True:
     print("Hello! You are currently using the Beta version of the 'Sausage' chat bot.")
     c = input("Enter a question in the input field: ")
     if c == "Hello":
         print("Hello! How can I help you?")
     elif c == "How are you?":
         print("Everything is fine. How about you?")
     elif c == "Bye":
         print("Goodbye!")
         break
     elif c == "Solve the example":
         calc11 = float(input("Number 1: "))
         calc22 = float(input("Number 2: "))
         calc33 = input("What to do (+,-,/,*): ")
     if calc33 == "+":
         answer1 = (calc11 + calc22)
         print(str(answer1))
         print("This is the answer")
     elif calc33 == "-":
         answer1 = (calc11 - calc22)
         print(str(answer1))
         print("This is the answer")
     elif calc33 == "/":
         answer1 = (calc11 / calc22)
         print(str(answer1))
         print("This is the answer")
     elif calc33 == "*":
         answer1 = (calc11 * calc22)
         print(str(answer1))
         print("This is the answer")
        

''')
                 else:
                     print("Sorry, you chose the wrong command.")
         elif a == "games":
             print("Factory owner simulator game")
             d = input("Enter the game you want to play: ")
             if d == "factory owner simulator":
                 dengi = 1000
                 product = 10
                 corpusov = 2
                 popy = 2
                 place1 = 100
                 mesta2 = mesta1 - product
                 print(''' SSSSSSSSSSS
  SS
 SS
SS
SS
SS
SS
SS
  SS
   SS
    SSSSSSSSSSS''')
                 while True:
                     print('You have ', product, ' pieces of product')
                     print('You have ', corpusov, ' hull(s)')
                     print('You have ', dengi, ' money')
                     print('You have ', popy, '% popularity')
                     print('You have left', mesta2, ' places in the shelves from ', mesta1, 'places')
                     deistvie = input("Enter action(For help, enter action 'Help'): ")
                     if deistvie == "build body":
                         a1 = dengi - 100
                         a2 = corpusov + 1
                         a3 = product + 40
                         qm = mesta2 - 40
                         dengi = a1
                         corpusov = a2
                         product = a3
                         mesta2 = qm
                     elif deistvie == "sell a product":
                         b1 = dengi + 110
                         b2 = product - 1
                         b3 = mesta2 + 1
                         dengi = b1
                         product = b2
                         place2 = b3
                     elif deistvie == "create a product":
                         c1 = product + 1
                         c2 = dengi - 15
                         c3 = place2 - 1
                         product = c1
                         dengi = c2
                         place2 = c3
                     elif deistvie == "demolish the body":
                         d1 = corpusov - 1
                         d2 = dengi - 8
                         d3 = mesta2 + 40
                         d4 = product - 40
                         product = d4
                         corpusov = d1
                         dengi = d2
                         place2 = d3
                     elif deistvie == "demolish the factory":
                         print("Your factory was demolished, and you don't have enough money to eat properly.")
                         print("Game Over")
                         input("")
                         break
                     elif deistvie == "charity":
                         print("How much do you want to give to charity?")
                         blag = input("Enter the amount (150, 200, 250, 300 money): ")
                         if blag == "150":
                             print("Do you mean Whitley the crab?")
                             qa = popy + 1
                             qb = dengi - 150 + 300
                             popy = qa
                             dengi = qb
                         elif blag == "200":
                             print("Porridge Hercules and sausage Papa can change the same arrow ten times better than in two versions of the Portal.")
                             qc = popy + 2
                             qd = dengi - 200 + 350
                             popy = qc
                             dengi = qd
                         elif blag == "250":
                             print("Pandas eat Hercules porridge!!!!!")
                             qe = popy + 3
                             qf = dengi - 250 + 400
                             popy = qe
                             dengy = qf
                         elif blag == "300":
                             print("Hurray! Pokos don't explode anymore!")
                             qg = popy + 5
                             qq = dengi - 300 + 450
                             popy = qg
                             dengi = qq
                     elif deistvie == "help":
                         print('''

There is a charity action, demolish the factory (end of the game), demolish the building,
create a product, sell a product, expand a warehouse and build a building.


''')
                     elif deistvie == "expand warehouse":
                         jh = dengi - 50
                         ji = place1 + 25
                         dengi = jh
                         place1 = ji
                     else:
                         print("You have been fined 25 money for illegal actions. Even Bloptop or Xiaomi do not break the laws.")
                         print(''' |||| ||||
       |||| ||||


     ------------------
   /\
  | |
         ''')
                         qr = dengi - 25
                         dengi = qr
                     if dengi == 0:
                         break
                     if mesta2 > mesta1:
                         print("Your space is full.")
                         print("Game Over")
                         input("")
                         break
         elif a == "time":
             o = time.localtime()
             ya = o[0]
             yb = o[1]
             yc = o[2]
             yd = o[3]
             ye = o[4]
             yg = o[5]
             print("It is ", ya, "year", yb, "month", yc, "day", yd, "hour(s), ", ye, "minutes and ", yg, "seconds.")
         elif a == "open program":
             import os
             bb = input("Enter the program you want to run: ")
             print('''
        

You can open programs such as:
        
Windows calculator;
Windows Explorer;
python;
Windows Notepad;
Windows control panel;
Windows Device Manager;
Windows Media Player;
DirectX Windows Diagnostic Tool;
Windows task manager.
processor control panel


''')
             if bb == "Windows calculator":
                 os.system("calc")
             elif bb == "Windows Explorer":
                 os.system("explorer")
             elif bb == "python":
                 os.system("python")
             elif bb == "Windows Notepad":
                 os.system("notepad")
             elif bb == "Windows command line":
                 os.system("cmd")
             elif bb == "Windows Control Panel":
                 os.system("control")
             elif bb == "Windows Device Manager":
                 os.system("devmgmt")
             elif bb == "Windows Media Player":
                 os.system("dvdplay")
             elif bb == "DirectX Windows Diagnostic Tool":
                 os.system("dxdiag")
             elif bb == "Windows task manager":
                 os.system("LaunchTM")
             elif bb == "processor control panel":
                 os.system("GfxUI")
             else:
                 print("You have selected a program that cannot be opened.")
         else:
             print("Sorry, you chose the wrong command.")
elif x1 == "中国人":
     print('''   SSSSSSSSSSS
  SS
 SS
SS
SS
SS
SS
SS
  SS
   SS
    SSSSSSSSSSS''')
     print('''


计算器命令 - 解决示例
版本命令 - 给出 RusDos 版本
记事本命令 - 保存您写入的内容（注意！在该命令中，一旦您向插槽中写入内容，就无法删除它（如果您在程序位置没有找到数据文件））
Komanda 聊天机器人是一个可以与您交谈的机器人
游戏团队 - 你可以玩游戏了（终于！！！！！！）
时间命令 - 以秒为单位精确显示时间
打开程序1号的命令 - 可以打开Windows中的任何程序（系统（其他程序根本不起作用（您安装的（程序））））


''')
     while True:
         a = input("输入命令: ")
         if a == "计算器":
             calc1 = float(input("1号: "))
             calc2 = float(input("1号: "))
             calc3 = input("该怎么办 (+,-,/,*): ")
             if calc3 == "+":
                 answer1 = (calc1 + calc2)
                 print(str(answer1))
                 print("这就是答案")
             if calc3 == "-":
                 answer1 = (calc1 - calc2)
                 print(str(answer1))
                 print("这就是答案")
             if calc3 == "/":
                 answer1 = (calc1 / calc2)
                 print(str(answer1))
                 print("这就是答案")
             if calc3 == "*":
                 answer1 = (calc1 * calc2)
                 print(str(answer1))
                 print("这就是答案")
         elif a == "版本":
             print("版本 RusDos（俄罗斯磁盘操作系统）7.2")
         elif a == "记事本":
             b = input("你想做什么（读槽（读）或在那里另外写一些东西（写）（注意：如果你想再写一行，那么不要按回车键！）。（要退出，请写“退出”（ 完全退出）））？ 在输入字段中输入解决方案: ")
             if b == "写":
                 b21 = input("选择插槽（从 1 到 5）: ")
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
                 elif b21 == "6":
                    test_file = open('c:\\RusDos\\6.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 elif b21 == "7":
                    test_file = open('c:\\RusDos\\7.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 elif b21 == "8":
                    test_file = open('c:\\RusDos\\8.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 elif b21 == "9":
                    test_file = open('c:\\RusDos\\9.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 elif b21 == "10":
                    test_file = open('c:\\RusDos\\10.txt', 'w')
                    test_file.write(b31)
                    test_file.close()
                 else:
                     print("抱歉，您选择了错误的录音槽位.")
             elif b == "读":
                 b22 = input("选择插槽（从 1 到 5）: ")
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
                 elif b22 == "6":
                    test_file = open('c:\\RusDos\\6.txt')
                    print(test_file.read())
                 elif b22 == "7":
                    test_file = open('c:\\RusDos\\7.txt')
                    print(test_file.read())
                 elif b22 == "8":
                    test_file = open('c:\\RusDos\\8.txt')
                    print(test_file.read())
                 elif b22 == "9":
                    test_file = open('c:\\RusDos\\9.txt')
                    print(test_file.read())
                 elif b22 == "10":
                    test_file = open('c:\\RusDos\\10.txt')
                    print(test_file.read())
                 else:
                     print("抱歉，您选择了错误的阅读时段.")
             elif b == "出口":
                 break
         elif a == "聊天机器人":
             while True:
                 print("你好！ 您当前使用的是“Sausage”聊天机器人的测试版.")
                 c = input("在输入字段中输入问题: ")
                 if c == "你好":
                     print("你好！ 我怎么帮你？")
                 elif c == "你好吗？":
                     print("一切安好。 你呢?")
                 elif c == "我很好":
                     print("伟大的！")
                 elif c == "再见":
                     print("再见!")
                     break
                 elif c == "解决例子":
                     calc11 = float(input("数字 1: "))
                     calc22 = float(input("数字 2: "))
                     calc33 = input("该怎么办 (+,-,/,*): ")
                     if calc33 == "+":
                         answer1 = (calc11 + calc22)
                         print(str(answer1))
                         print("这就是答案")
                     elif calc33 == "-":
                         answer1 = (calc11 - calc22)
                         print(str(answer1))
                         print("这就是答案")
                     elif calc33 == "/":
                         answer1 = (calc11 / calc22)
                         print(str(answer1))
                         print("这就是答案")
                     elif calc33 == "*":
                         answer1 = (calc11 * calc22)
                         print(str(answer1))
                         print("这就是答案")
                 elif c == "你的代码是什么？":
                     print('''   很简单！ 只需安装Python，然后复制这个:



while True:
                 print("你好！ 您当前使用的是“Sausage”聊天机器人的测试版.")
                 c = input("在输入字段中输入问题: ")
                 if c == "你好":
                     print("你好！ 我怎么帮你？")
                 elif c == "你好吗？":
                     print("一切安好。 你呢?")
                 elif c == "我很好":
                     print("伟大的！")
                 elif c == "再见":
                     print("再见!")
                     break
                 elif c == "解决例子":
                     calc11 = float(input("数字 1: "))
                     calc22 = float(input("数字 2: "))
                     calc33 = input("该怎么办 (+,-,/,*): ")
                     if calc33 == "+":
                         answer1 = (calc11 + calc22)
                         print(str(answer1))
                         print("这就是答案")
                     elif calc33 == "-":
                         answer1 = (calc11 - calc22)
                         print(str(answer1))
                         print("这就是答案")
                     elif calc33 == "/":
                         answer1 = (calc11 / calc22)
                         print(str(answer1))
                         print("这就是答案")
                     elif calc33 == "*":
                         answer1 = (calc11 * calc22)
                         print(str(answer1))
                         print("这就是答案")
        

''')
                 else:
                     print("抱歉，您选择了错误的命令.")
         elif a == "游戏":
             print("工厂主模拟器游戏")
             d = input("工厂主模拟器游戏: ")
             if d == "工厂主模拟器":
                 dengi = 1000
                 product = 10
                 corpusov = 2
                 popy = 2
                 place1 = 100
                 mesta2 = mesta1 - product
                 print(''' SSSSSSSSSSS
  SS
 SS
SS
SS
SS
SS
SS
  SS
   SS
    SSSSSSSSSSS''')
                 while True:
                     print('你有 ', product, ' pieces of product')
                     print('你有 ', corpusov, ' hull(s)')
                     print('你有 ', dengi, ' money')
                     print('你有 ', popy, '% popularity')
                     print('你已经离开了', mesta2, ' 货架上的位置来自 ', mesta1, 'places')
                     deistvie = input("输入操作（如需帮助，请输入操作“帮助”）: ")
                     if deistvie == "塑造身体":
                         a1 = dengi - 100
                         a2 = corpusov + 1
                         a3 = product + 40
                         qm = mesta2 - 40
                         dengi = a1
                         corpusov = a2
                         product = a3
                         mesta2 = qm
                     elif deistvie == "销售产品":
                         b1 = dengi + 110
                         b2 = product - 1
                         b3 = mesta2 + 1
                         dengi = b1
                         product = b2
                         place2 = b3
                     elif deistvie == "创建一个产品":
                         c1 = product + 1
                         c2 = dengi - 15
                         c3 = place2 - 1
                         product = c1
                         dengi = c2
                         place2 = c3
                     elif deistvie == "拆除身体":
                         d1 = corpusov - 1
                         d2 = dengi - 8
                         d3 = mesta2 + 40
                         d4 = product - 40
                         product = d4
                         corpusov = d1
                         dengi = d2
                         place2 = d3
                     elif deistvie == "拆除工厂":
                         print("你的工厂被拆了，你连吃饭的钱都没有。")
                         print("游戏结束")
                         input("")
                         break
                     elif deistvie == "慈善机构":
                         print("你想捐多少钱给慈善机构?")
                         blag = input("输入金额（150、200、250、300 钱）): ")
                         if blag == "150":
                             print("你是说螃蟹惠特利吗?")
                             qa = popy + 1
                             qb = dengi - 150 + 300
                             popy = qa
                             dengi = qb
                         elif blag == "200":
                             print("粥赫拉克勒斯和香肠爸爸可以比在两个版本的传送门中更好地改变同一个箭头十倍。")
                             qc = popy + 2
                             qd = dengi - 200 + 350
                             popy = qc
                             dengi = qd
                         elif blag == "250":
                             print("熊猫吃大力神粥！！！！")
                             qe = popy + 3
                             qf = dengi - 250 + 400
                             popy = qe
                             dengy = qf
                         elif blag == "300":
                             print("Poco不再爆炸了！")
                             qg = popy + 5
                             qq = dengi - 300 + 450
                             popy = qg
                             dengi = qq
                     elif deistvie == "帮助":
                         print('''

有一个慈善行动，拆工厂（游戏结束），拆建筑，
创建产品、销售产品、扩建仓库和建造建筑物。


''')
                     elif deistvie == "扩大仓库":
                         jh = dengi - 50
                         ji = place1 + 25
                         dengi = jh
                         place1 = ji
                     else:
                         print("您因违法行为被罚款25元。 即使是 Bloptop 或小米也不违法")
                         print(''' |||| ||||
       |||| ||||


     ------------------
   /\
  | |
         ''')
                         qr = dengi - 25
                         dengi = qr
                     if dengi == 0:
                         break
                     if mesta2 > mesta1:
                         print("你的空间已满.")
                         print("游戏结束")
                         input("")
                         break
         elif a == "时间":
             o = time.localtime()
             ya = o[0]
             yb = o[1]
             yc = o[2]
             yd = o[3]
             ye = o[4]
             yg = o[5]
             print("这是 ", ya, "年", yb, "月", yc, "日", yd, "小时), ", ye, "分钟 和 ", yg, "秒.")
         elif a == "开放程序":
             import os
             bb = input("输入您要运行的程序: ")
             print('''
        

您可以打开以下程序：
        
Windows 计算器；
Windows资源管理器;
Python;
Windows 记事本；
Windows 控制面板；
Windows 设备管理器；
Windows 媒体播放器;
DirectX Windows 诊断工具；
Windows 任务管理器。
处理器控制面板

''')
             if bb == "Windows 计算器":
                 os.system("calc")
             elif bb == "Windows资源管理器":
                 os.system("explorer")
             elif bb == "Python":
                 os.system("python")
             elif bb == "Windows 记事本":
                 os.system("notepad")
             elif bb == "Windows 控制面板":
                 os.system("control")
             elif bb == "Windows 设备管理器":
                 os.system("devmgmt")
             elif bb == "Windows 媒体播放器":
                 os.system("dvdplay")
             elif bb == "DirectX Windows 诊断工具；":
                 os.system("dxdiag")
             elif bb == "Windows 任务管理器。":
                 os.system("LaunchTM")
             elif bb == "处理器控制面板":
                 os.system("GfxUI")
             else:
                 print("您选择了无法打开的程序.")
         else:
             print("抱歉，您选择了错误的命令.")
