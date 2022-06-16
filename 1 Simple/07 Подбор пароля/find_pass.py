stroka_find = input(str("Введите 10 знач строку:"))
stroka = ""
alphabet = []
for i in range (65,91):
    alphabet.append(chr(i))
for i in range (97,123):
    alphabet.append(chr(i))
print(alphabet)
for a0 in range (len(alphabet)):
    for a1 in range (len(alphabet)):
        for a2 in range(len(alphabet)):
            for a3 in range(len(alphabet)):
                for a4 in range(len(alphabet)):
                    for a5 in range(len(alphabet)):
                        for a6 in range(len(alphabet)):
                            for a7 in range(len(alphabet)):
                                for a8 in range(len(alphabet)):
                                    for a9 in range(len(alphabet)):
                                        stroka = alphabet[a0] + alphabet[a1] + alphabet[a2] + alphabet[a3] + alphabet[a4] + alphabet[a5] + alphabet[a6] + alphabet[a7] + alphabet[a8] + alphabet[a9]
                                        #print("Промежуточное значение:",stroka)
                                        if stroka == stroka_find:
                                            break
                                    if stroka == stroka_find:
                                        break
                                if stroka == stroka_find:
                                    break
                            if stroka == stroka_find:
                                break
                        if stroka == stroka_find:
                            break
                    if stroka == stroka_find:
                        break
                if stroka == stroka_find:
                    break
            if stroka == stroka_find:
                break
        if stroka == stroka_find:
            break
    if stroka == stroka_find:
        break

print("Искомое значение найдено:",stroka)
