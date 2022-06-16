mas=[]
mas1=[]
mas2=[]

def vvod_dannykh():
    global a,b,str
    print("Введите a и b. Внимание- a и 27 должны быть взаимно простыми, так же a должно быть меньше 27!")
    a = 0
    while a == 0:
        print("Введите a:", end="\t")
        a = int(input())
        for i in range(2, (a + 1), 1):
            if 27 % i == 0 and a % i == 0 and a >= 27:
                a = 0
    print("Введите b:", end="\t")
    b = int(input())
    print("Введите строку на английском языке строчными буквами:", end="\t")
    str = str(input())

def shifr():
    global a,b,mas,mas1,mas2,str
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    for i in range(len(str)):
        mas.append(str[i])
        mas1.append(str[i])
    for i in range (len(mas)):
        for j in range (27):
            if mas[i]==alphabet[j]:
                mas[i]=j
                mas1[i]=j
    for i in range (len(mas1)):
        mas1[i]=(((mas1[i]*a)+b)%27)
    for i in range(len(mas1)):
        mas2.append(mas1[i])
    for i in range (len(mas2)):
        for j in range (27):
            if mas2[i]==j:
                mas2[i]=alphabet[j]


vvod_dannykh()
shifr()
print("Каждой букве присваиваем порядковый номер по алфавиту:",*mas)
print("Зашифровываем в цифрах:",*mas1)
print("Зашифровываем в буквах:",*mas2)
str2=""
for i in range (len(mas2)):
    str2+=(mas2[i])
print("Зашифрованный текст:",str2)
