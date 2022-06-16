to_rome = int(input("Введите 1 для перевода в Римскую систему счисления, 0 для перевода из Римской в десятичную:"))
if to_rome == 1:
    check = 0
    while check == 0:
        input_number = str(input(("Введите изначальное число в десятичной системе счисления:")))
        if 0 < int(input_number) < 4000:
            check = 1
        else:
            print ("Введено неправильное значение. Перевести в Римскую систему счисления можно только числа в диапазоне от 1 до 3999.")
else:
    input_number = str(input(("Введите изначальное число в Римской системе счисления:")))
output_number = ""
input = input_number
temp=""

def to_rome_calc():
    global input_number, output_number
    poryadok_10 = 0
    for i in range (len(input_number),0,-1):
        i -= 1
        temp = ""
        if poryadok_10 == 0:
            if input_number[i] == "1":
                temp = "I"
            if input_number[i] == "2":
                temp = "IIIV"
            if input_number[i] == "3":
                temp = "IIV"
            if input_number[i] == "4":
                temp = "IV"
            if input_number[i] == "5":
                temp = "V"
            if input_number[i] == "6":
                temp = "VI"
            if input_number[i] == "7":
                temp = "VII"
            if input_number[i] == "8":
                temp = "VIII"
            if input_number[i] == "9":
                temp = "IX"

        if poryadok_10 == 1:
            if input_number[i] == "1":
                temp = "X"
            if input_number[i] == "2":
                temp = "XXXL"
            if input_number[i] == "3":
                temp = "XXL"
            if input_number[i] == "4":
                temp = "XL"
            if input_number[i] == "5":
                temp = "L"
            if input_number[i] == "6":
                temp = "LX"
            if input_number[i] == "7":
                temp = "LXX"
            if input_number[i] == "8":
                temp = "LXXX"
            if input_number[i] == "9":
                temp = "XC"

        if poryadok_10 == 2:
            if input_number[i] == "1":
                temp = "C"
            if input_number[i] == "2":
                temp = "CCCD"
            if input_number[i] == "3":
                temp = "CCD"
            if input_number[i] == "4":
                temp = "CD"
            if input_number[i] == "5":
                temp = "D"
            if input_number[i] == "6":
                temp = "DC"
            if input_number[i] == "7":
                temp = "DCC"
            if input_number[i] == "8":
                temp = "DCCC"
            if input_number[i] == "9":
                temp = "CM"

        if poryadok_10 == 3:
            if input_number[i] == "1":
                temp = "M"
            if input_number[i] == "2":
                temp = "MM"
            if input_number[i] == "3":
                temp = "MMM"

        output_number = temp + output_number
        poryadok_10 += 1

lengh = len(input_number)
def from_rome_calc():
    global temp,lengh
    poryadok_10 = 0
    while lengh > 0:
        i = lengh - 1
        temp_calc(i,poryadok_10)
        poryadok_10 += 1

def temp_calc(i,poryadok_10):
    global temp,input_number,lengh,output_number

    if poryadok_10 == 0:
        krat_1 = "I"
        krat_10 = "X"
        krat_5 = "V"
    if poryadok_10 == 1:
        krat_1 = "X"
        krat_10 = "C"
        krat_5 = "L"
    if poryadok_10 == 2:
        krat_1 = "C"
        krat_10 = "M"
        krat_5 = "D"
    if poryadok_10 == 3:
        krat_1 = "M"

    if input_number[i] == krat_1:
        if len(input_number) >= 2 and input_number[i - 1] == krat_1:
               if len(input_number) >= 3 and input_number[i - 2] == krat_1:
                   if poryadok_10 == 3:
                       temp = 3 * (10 ** poryadok_10)
                       lengh -= 3
                       input_number = input_number[0:lengh]
                       output_number = temp + output_number
                       return
                   else:
                       temp = 8*(10**poryadok_10)
                       lengh -= 4
                       input_number = input_number[0:lengh]
                       output_number = temp + output_number
                       return
               else:
                   temp = 7*(10**poryadok_10)
                   lengh -= 3
                   input_number = input_number[0:lengh]
                   output_number = temp + output_number
                   return
        else:
               if len(input_number) >= 2 and input_number[i - 1] == krat_5:
                   temp = 6*(10**poryadok_10)
                   lengh -= 2
                   input_number = input_number[0:lengh]
                   output_number = temp + output_number
                   return
               else:
                   temp = 1*(10**poryadok_10)
                   lengh -= 1
                   input_number = input_number[0:lengh]
                   output_number = temp + output_number
                   return

    if input_number[i] == krat_5:
         if len(input_number) >= 2 and input_number[i - 1] == krat_1:
             if len(input_number) >= 3 and input_number[i - 2] == krat_1:
                 if len(input_number) >= 4 and input_number[i - 2] == krat_1:
                     temp = 2*(10**poryadok_10)
                     lengh -= 4
                     input_number = input_number[0:lengh]
                     output_number = temp + output_number
                     return
                 else:
                     temp = 3*(10**poryadok_10)
                     lengh -= 3
                     input_number = input_number[0:lengh]
                     output_number = temp + output_number
                     return
             else:
                 temp = 4*(10**poryadok_10)
                 lengh -= 2
                 input_number = input_number[0:lengh]
                 output_number = temp + output_number
                 return
         else:
             temp = 5*(10**poryadok_10)
             lengh -= 1
             input_number = input_number[0:lengh]
             output_number = temp + output_number
             return

    if input_number[i] == krat_10:
        if len(input_number) >= 2 and input_number[i - 1] == krat_1:
            temp = 9 * (10 ** poryadok_10)
            lengh -= 2
            input_number = input_number[0:lengh]
            output_number = temp + output_number
            return
        else:
            temp = 10 * (10 ** poryadok_10)
            lengh -= 1
            input_number = input_number[0:lengh]
            output_number = temp + output_number
            return

if to_rome == 1:
    to_rome_calc()
else:
    output_number = 0
    from_rome_calc()

print("Число",input,"в переводе из десятичной системы счисления в римскую систему счисления:",output_number)
