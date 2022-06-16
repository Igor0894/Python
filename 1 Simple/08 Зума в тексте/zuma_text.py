import random
stroka="    "
stroka_pos = "pos= "
inp = 1
shot = 0

def clear():
    global stroka
    i = 4
    while i < len(stroka) - 2:
        print("stroka[i]=",stroka[i],"stroka[i+2]=",stroka[i+2])
        if stroka[i] == stroka[i+2]:
            offset = 2
            while i + offset < len(stroka) and stroka[i] == stroka[i + offset]:
                offset += 2
            stroka = stroka[0:i] + stroka[i + offset:]
            i = 4
            print("i=",i,"stroka=",stroka)
        i += 2

for i in range (10):
    r = random.randint(1,9)
    stroka += str(r)
    stroka += "-"
    stroka_pos += str(i + 1) + " "


while len(stroka) > 0:
    print(stroka)
    print(stroka_pos)
    shot = random.randint(1, 9)
    print("Сгенерирована цифра:",shot)
    inp = input("Вставка в позицию (нижняя строка):")
    inp = int(inp)
    stroka = stroka[:(2 * inp) + 3] + "-" + str(shot) + "-" + stroka[(2 * inp) + 4:]
    print ("Получившаяся строка до сокращения:",stroka)
    clear()
