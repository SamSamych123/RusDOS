import pickle
import time

a = input("Введите пароль: ")
passworld = open('passworld.dat', 'wb')
pickle.dump(a, passworld)
passworld.close()
aa = input("Введите пароль ещё раз: ")
if aa == a:
    print("Спасибо за создание пароля для RusDos!")
    time.sleep(3)
else:
    print("Неправильно набран пароль!")
    time.sleep(3)
