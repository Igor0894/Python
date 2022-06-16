s_in = int(input("Введите изначальную систему счисления:"))
s_out = int(input("Введите желаемую систему счисления:"))
input_number = str(input(("Введите изначальное число:")))
input_number1 = input_number
output_number = 0
temp = 0
cifr = ["0","1","2","3","4","5","6","7","8","9"]

def from_S_IN_to10(s_in,num):
    global cifr
    res = 0
    for i in range(len(num)):
        if num[i] in cifr:
            res += int(num[i]) * (s_in ** (len(num) - i - 1))
        else:
            res += (ord(num[i]) - 65 + 10) * (s_in ** (len(num) - i - 1))
    return res

def from_10_to_S_OUT(s_out,num):
    res = ""
    while num > 0:
        r = num % s_out
        num = num // s_out
        if r < 10:
            res = str(r) + res
        else:
            if r == 10:
                res = "A" + res
            if r == 11:
                res = "B" + res
            if r == 12:
                res = "C" + res
            if r == 13:
                res = "D" + res
            if r == 14:
                res = "E" + res
            if r == 15:
                res = "F" + res
    return res

if s_out == 10:
    output_number = from_S_IN_to10(s_in,input_number)
elif s_in == 10:
    input_number = int(input_number)
    output_number = from_10_to_S_OUT(s_out,input_number)
else:
    input_number = from_S_IN_to10(s_in,input_number)
    output_number = from_10_to_S_OUT(s_out,input_number)

print("Число",input_number1,"в переводе из",s_in,"в",s_out,"систему счисления:",output_number)
