mass = []
a = 0
deep = 0
max_deep = 0

def read():
    global a,mass,deep
    add_a = 0
    a = (input("Введите значение:"))
    if a == ".":
        return
    a = int(a)
    mass,add_a,deep = add_element(mass,add_a,deep)
    if add_a == 0:
        mass_in_mass(mass,add_a,deep)
    else:
        print("Добавлено значение=", a)
        print("mass=",mass)


def add_element(mas,add_a,deep):
    global a, max_deep
    if len(mas) > 0:
        print("Начало, mas=", mas)
        print("a=", a)

        if len(mas) > 1:
            #print("Mas1=", mas[1])
            #print("Mas2=", mas[2])
            if len(mas) > 1 and mas[2] == 0 and a > mas[0]:
                mas[2] = a
                print("Подстановка, mas=",mas)
                return mas,1,deep
            if mas[1] == 0 and a < mas[0]:
                mas[1] = a
                print("Подстановка, mas=", mas)
                return mas,1,deep

        if len(mas) == 1:
            print("Заход в расширение неполного массива, mas=", mas)
            if a > mas[0]:
                mas = [mas[0],0,a]
            else:
                mas = [mas[0],a,0]
            print("Выход из расширения, mas=", mas)
            return mas,1,deep

        for i in range (len(mas)):
            if (isinstance(mas[i],list)):
                print("Вход в рекурсию, mas[i]=", mas[i])
                deep += 1
                if deep > max_deep:
                    max_deep = deep
                print("Глубина=", deep)
                mas[i],add_a,deep = add_element(mas[i],0,deep)
                deep -= 1
                print("Выход из рекурсии, mas=",mas)
                print("Глубина=", deep)
                if add_a == 1:
                    break

        if add_a == 0:
            #print("Заход в расширение полного массива, mas0=", mas[0])
            #if isinstance(mas[2],int) and a > mas[2] and mas[2] != 0:
            #    mas[2] = [mas[2], 0, a]
            #    print("Выход из расширения, mas=", mas)
            #    return mas,1,deep
            #if isinstance(mas[1],int) and a < mas[1]:
            #    mas[1] = [mas[1], a, 0]
            #    print("Выход из расширения, mas=", mas)
            #    return mas,1,deep
            return mas,0,deep
        else:
            return mas,add_a,deep

    else:
        mas.append(a)
        print(a," голова")
        return mas,1,deep

def mass_in_mass(mas,add_a,deep):
    global a,max_deep
    print("Заход в расширение полного массива, mas=", mas)
    for i in range(1,len(mas)):
        if (isinstance(mas[i],int)):
            if a > mas[i] and mas[i] != 0:
                mas[i] = [mas[i], 0, a]
                print("Выход из расширения, mas=", mas)
                return mas, 1, deep
            if a < mas[i] and mas[i] != 0:
                mas[i] = [mas[i], a, 0]
                print("Выход из расширения, mas=", mas)
                return mas, 1, deep
    for i in range(len(mas)):
        if (isinstance(mas[i],list)):
            deep += 1
            print("Вход в рекурсию расширения полного массива, mas[i]=", mas[i])
            print("Глубина=", deep)
            mass_in_mass(mas[i],add_a,deep)
            deep -= 1
            print("Выход из рекурсии расширения полного массива, mas=", mas)
            print("Глубина=", deep)
            if add_a == 1:
                break




while a != ".":
    read()
