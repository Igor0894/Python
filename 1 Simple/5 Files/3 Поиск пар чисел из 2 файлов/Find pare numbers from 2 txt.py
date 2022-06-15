stroka=str()
mas=[]
sum=0
chetn=0
nechetn=0
chetn_sum=0
chetn_most=0
min=0
max=0
spisok=[]

def open_file():
    global spisok
    spisok = open('C:/test/text5b.txt').read()
    spisok = spisok.splitlines()
    print("Колличество пар в наборе:",spisok[0])
    spisok.pop(0)
    for i in range(len(spisok)):
        spisok[i] = spisok[i].split(" ")
        spisok[i][0],spisok[i][1]=int(spisok[i][0]),int(spisok[i][1])

def f_chetn_sum():
    global sum, chetn_sum
    if sum%2==0:
        chetn_sum=1
    else:
        chetn_sum=0

def f_chetn_most():
    global mas,chetn_most,chetn,nechetn
    chetn=0
    nechetn=0
    string=str()
    nums=0
    sum=0
    digit=int()
    for i in range (len(mas)):
        if mas[i]%2==0:
            chetn+=1
        else:
            nechetn+=1
    if chetn>=nechetn:
        chetn_most=1
    else:
        chetn_most=0

def sravn(a,fl):
    if (a[0]<a[1] and fl==1) or (a[0]>a[1] and fl==0):
        return a[0]
    if (a[0]>a[1] and fl==1) or (a[0]<a[1] and fl==0):
        return a[1]

def sum_mins():
    global spisok,stroka,min,sum
    for i in range(len(spisok)):
        stroka=spisok[i]
        min=sravn(stroka,1)
        sum+=min
        mas.append(min)
    f_chetn_sum()
    f_chetn_most()

def find_min_delta():
    global mins_bad,mins_bad_ind,sum,min,max,mas,spisok
    min_delta=sum
    min_delta_ind=0
    min_delta_max=0
    min_delta_min=0
    delta=0
    f=open('C:/test/text5b.txt','r')
    for i in range (len(spisok)):
        stroka = spisok[i]
        min = sravn(stroka, 1)
        max = sravn(stroka, 0)
        if min%2!=max%2:
            delta=(max-min)
            if delta<min_delta:
                min_delta=delta
                min_delta_ind=i
                min_delta_max=max
                min_delta_min=min
    mas[min_delta_ind]=min_delta_max
    #print("sum do=",sum)
    sum=sum-min_delta_min+min_delta_max
    #print("min_delta_ind=",min_delta_ind)
    #print("min_delta_max=",min_delta_max)
    #print("min_delta=", min_delta)
    #print("zanchenie v mas gde min delta=",mas[min_delta_ind])

open_file()
print("Первоначальный массив:",spisok)
sum_mins()
#print("ДО Сумма чётная-true=",chetn_sum)
#print("ДО Большинство чётные-true=",chetn_most)
#print("ДО Чётных элементов=",chetn)
#print("ДО Нечётных элементов=",nechetn)
#print("ДО Минимальная сумма",sum)
while chetn_sum!=chetn_most:
    find_min_delta()
    f_chetn_sum()
    f_chetn_most()
print("Получившийся массив=", mas)
print("Колличество элементов массива=",len(mas))
print("Сумма чётная-true=",chetn_sum)
print("Большинство чётные-true=",chetn_most)
print("Чётных элементов=",chetn)
print("Нечётных элементов=",nechetn)
print("Минимальная сумма",sum)
