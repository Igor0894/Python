class stek():
    mas = []
    def push(self,el):
        self.mas.append(el)
    def pushandcheck(self,el):
        if  len(self.mas)>0:
            if el == ")" and self.mas[-1] == "(":
                self.pop()
            elif el == "}" and self.mas[-1] == "}":
                self.pop()
            elif el == "[" and self.mas[-1] == "]":
                self.pop()
            else:
                self.push(el)
        else:
            self.push(el)
    def pop(self):
        print(self.mas[len(self.mas) - 1])
        self.mas.pop(-1)
    def show(self):
        print(self.mas[-1])
    def count(self):
        print("Колличество элементов в стеке:", len(self.mas))

inp = 1
st = stek()
s="{}{}([()()])"
for i in range(len(s)):
    st.pushandcheck(s[i])
print(st.mas)
