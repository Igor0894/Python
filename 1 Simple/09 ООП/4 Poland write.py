class stek():
    mas = []
    operations = ["+","-","*","/"]
    def push(self,stroka):
        self.mas = stroka.split(" ")
    def pop(self):
        print(self.mas[len(self.mas)-1])
        self.mas.pop(len(self.mas)-1)
    def show(self):
        print(self.mas)
    def count(self):
        calc = 0
        arg_a = "clear"
        arg_b = "clear"
        while len(self.mas) > 1:
            for i in range(len(self.mas)):
                if self.mas[i] not in self.operations:
                    print(self.mas[i],"not in operations")
                if self.mas[i] in self.operations:
                    print(self.mas[i],"in operations")
                if calc == 1:
                    arg_a = "clear"
                    arg_b = "clear"
                    calc = 0
                if (self.mas[i] not in self.operations) and arg_a == "clear":
                    arg_a = self.mas[i]
                    print("arg_a=",arg_a)
                elif (self.mas[i] not in self.operations) and arg_b == "clear":
                    arg_b = self.mas[i]
                    print("arg_b=", arg_b)
                elif (self.mas[i] not in self.operations) and arg_b != "clear":
                    arg_a = arg_b
                    print("arg_a=", arg_a)
                    arg_b = self.mas[i]
                    print("arg_b=", arg_b)
                else:
                    calculate = eval(arg_a + self.mas[i] + arg_b)
                    print("Операция",arg_a,self.mas[i],arg_b,"=",calculate)
                    self.mas[i] = str(calculate)
                    self.mas.pop(i - 1)
                    self.mas.pop(i - 2)
                    calc = 1
                    break



def showmenu():
    print("[1] Записать строку в стек")
    print("[2] Показать значения стека")
    print("[3] Вычислить строку")
    print("[0] Выход")

inp = 1
s = stek()
while inp != 0:
    showmenu()
    inp = int(input("Выберете пункт меню:"))
    print()
    if inp == 0:
        break
    elif inp == 1:
        stroka = input("Введите строку для вычисления с пробелами:")
        s.push(stroka)
    elif inp == 2:
        s.show()
    elif inp == 3:
        s.count()
    print()
