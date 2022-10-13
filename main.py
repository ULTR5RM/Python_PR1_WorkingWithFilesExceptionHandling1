while True:
    print("Введите '+' для добавления данных, и '-' для выхода из программы")
    cheak: str = input()
    if cheak in ["+"]:
        try:
            print('Введите ФИО и год рождения через пробел:')
            Surname, Name, Patronymic, Year = map(str, input().split())
            print(f"Вы ввели: {Surname} {Name} {Patronymic} {Year}")
            assert Year.isdigit()
        except ValueError:
            print('Не правильно внесены данные!')
        except:
            print('Ошибка!')
        try:
            File = open("Data.txt", "a", encoding='utf8')
            File.write(f"{Surname} {Name} {Patronymic} {Year}\n")
            File.close()
        except PermissionError:
            print('Нет доступа')
        except:
            print('Ошибка!')
    else:
        if cheak in ['-']:
            print("Запись в файл завершена")
            exit()
        else:
            print("Ошибка")
            exit()
