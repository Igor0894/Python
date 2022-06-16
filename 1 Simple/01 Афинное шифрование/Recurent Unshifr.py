mas=[]
mas1=[]
mas2=[]

def vvod_dannykh():
    global a,a1,a2,b1,b2,str
    print("Введите a1,a2 и b1,b2. Внимание- a1,a2 и 27 должны быть взаимно простыми, так же a1,a2 должно быть меньше 27!")
    a1= 0
    while a1==0:
        print("Введите a1:",end="\t")
        a1=int(input())
        for i in range(2,(a1+1),1):
            if 27%i==0 and a1%i==0 or a1>=27:
                a1=0
    print("Введите b1:",end="\t")
    b1=int(input())

    a2=0
    while a2==0:
        print("Введите a2:",end="\t")
        a2=int(input())
        for i in range(2,(a2+1),1):
            if 27%i==0 and a2%i==0 or a2>=27:
                a2=0
    print("Введите b2:",end="\t")
    b2=int(input())

    print("Введите строку зашифрованную рекуррентный аффинным шифром на английском языке строчными буквами:", end="\t")
    str = str(input())

def kluch_a(i):
    global a1,a2
    if i==0:
        a=a1
    if i==1:
        a=a2
    if i>=2:
        a=(a1*a2)%27
        a1=a2
        a2=a
    return a

def kluch_b(i):
    global b1,b2
    if i==0:
        b=b1
    if i==1:
        b=b2
    if i>=2:
        b=(b1+b2)%27
        b1=b2
        b2=b
    return b

def a_obr(x):
    a=0
    while ((a*x)%27)!=1:
        a+=1
    return a


def shifr():
    global mas,mas1,mas2,str
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
        a=kluch_a(i)
        b=kluch_b(i)
        a1=a_obr(a)
        mas1[i]=((a1*(mas1[i]+27-b))%27)
    for i in range(len(mas1)):
        mas2.append(mas1[i])
    for i in range (len(mas2)):
        for j in range (27):
            if mas2[i]==j:
                mas2[i]=alphabet[j]


vvod_dannykh()
shifr()
print("Каждой букве присваиваем порядковый номер по алфавиту:",*mas)
print("Расшифровываем в цифрах:",*mas1)
print("Расшифровываем в буквах:",*mas2)
str2=""
for i in range (len(mas2)):
    str2+=(mas2[i])
print("Расшифрованный текст:",str2)
