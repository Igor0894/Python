f = open('all.txt')
f2 = open('5symbols.txt', 'a')
try:
    for word in f.readlines():
        if len(word) == 6:
            print(word)
            ##f2.write(word + '\n')
            f2.write(word)
finally:
    f.close()
    f2.close()