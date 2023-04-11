"""1. Открыть файл
2. Сохранить файл
3. Посмотреть все контакты
4. Создать контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход"""

fileName = 'C:/Users/Ojgen/Desktop/Домашка/6/8/1.txt'

def open_cont():
    fileName = input('введите адрес файла')

def add_cont():
    file = open(fileName, 'a', encoding='UTF-8')
    file2 = open(fileName, 'r', encoding='UTF-8')
    data0 = file2.readlines()
    file2.close()
    if len(data0) == 0:
        data0 = 1
    else:
        data0 = int(data0[-1].strip().split(';')[0]) + 1
    data1 = input('введите ФИО')
    data2 = input('введите номер телефона')
    data3 = input('введите место работы')
    data = '\n' + str(data0) + ';' + data1 + ';' + data2 + ';' + data3
    print(data)
    file.write(data)
    file.close()

def read_cont():
    file = open(fileName, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        print(contact)

def find_cont():
    file = open(fileName, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    search_cont = input('введите информацию для поиска')
    for cont in data:
        if search_cont.lower() in cont.lower():
            print(cont)

def change_cont():
    file = open(fileName, 'r', encoding='UTF-8')
    id = int(input('введите id'))
    isFound = False
    
    lines = file.readlines()
    file.seek(0)
    data = file.read()

    for line in lines:
        if len(line) == 0:
            continue
        data0 = int(line.strip().split(';')[0])
        if data0 == id:
            isFound = True
            break

    if not isFound:
        print('не найдено')
        return
    
    data1 = input('введите ФИО')
    data2 = input('введите номер телефона')
    data3 = input('введите место работы')
    newData = str(id) + ';' + data1 + ';' + data2 + ';' + data3 + '\n'
    data = data.replace(line, newData)
    with open (fileName, 'w', encoding='UTF-8') as f:
        f.write(data)

    print(line)
    print(data)
   
def del_cont():
    file = open(fileName, 'r', encoding='UTF-8')
    id = int(input('введите id'))
    isFound = False
    
    lines = file.readlines()
    file.seek(0)
    data = file.read()

    for line in lines:
        if len(line) == 0:
            continue
        data0 = int(line.strip().split(';')[0])
        if data0 == id:
            isFound = True
            break
        
    if not isFound:
        print('не найдено')
        return

    data = data.replace(line, '')
    with open (fileName, 'w', encoding='UTF-8') as f:
        f.write(data)

    print(line)
    print(data)

def main():
    x = input ('''
    1. Открыть файл
    2. Сохранить файл
    3. Посмотреть все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход
    ''')
    match x:
        case "1":
            print("Открыть файл")
            open_cont()
        case "2":
            print("Нет такой команды")
        case "3":
            print("Посмотреть все контакты")
            read_cont()
        case "4":
            print("Создать контакт")
            add_cont()
        case "5":
            print("Найти контакт")
            find_cont()
        case "6":
            print("Изменить контакт")
            change_cont()
        case "7":
            print("Удалить контакт")
            del_cont()
        case "8":
            print("Выход")
            quit()
        case _:
            print("Команды не существует")
    main()

main()