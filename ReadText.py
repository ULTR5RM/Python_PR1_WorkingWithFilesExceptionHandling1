try:
    File = open("Data.txt", "r", encoding='utf8')
    for line in File:
        print(line)
except SyntaxError:
    print("Ошибка чтения файла!")
except:
    exit()