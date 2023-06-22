import csv

def read_contacts():
    contacts = []
    with open('contacts.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def write_contacts(contacts):
    with open('contacts.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def edit_contact(contacts):
    fam = input('Введите фамилию контакта для редактирования: ')
    found_contact = False
    for contact in contacts:
        if fam in contact[0]:
            field = input('Выберите поле для редактирования (1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, 5 - текст): ')
            if field == '1':
                new_value = input('Введите новую фамилию: ')
                contact[0] = new_value
            elif field == '2':
                new_value = input('Введите новое имя: ')
                contact[1] = new_value
            elif field == '3':
                new_value = input('Введите новое отчество: ')
                contact[2] = new_value
            elif field == '4':
                new_value = input('Введите новый номер: ')
                contact[3] = new_value
            elif field == '5':
                new_value = input('Введите новый текст: ')
                contact[4] = new_value
            else:
                print('Некорректное поле. Редактирование отменено.')
                return
            print('Контакт успешно отредактирован.')
            found_contact = True
            break
    if not found_contact:
        print('Контакт не найден.')

def delete_contact(contacts):
    fam = input('Введите фамилию контакта для удаления: ')
    updated_contacts = []
    for contact in contacts:
        if fam not in contact[0]:
            updated_contacts.append(contact)
    if len(updated_contacts) == len(contacts):
        print('Контакт не найден.')
    else:
        print('Контакт успешно удален.')
    return updated_contacts

def add_contact(contacts):
    fam = input('Введите фамилию: ')
    nam = input('Введите имя: ')
    ot = input('Введите отчество: ')
    numb = input('Введите номер: ')
    txt = input('Введите текст: ')
    contacts.append([fam, nam, ot, numb, txt])
    print('Контакт успешно добавлен.')

def search_contact(contacts):
    com_2 = input('Введите команду (1 - все контакты, 2 - поиск по фамилии): ')
    if com_2 == '1':
        if not contacts:
            print('Контакты не найдены.')
        else:
            for contact in contacts:
                print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер: {contact[3]}, Текст: {contact[4]}")
    elif com_2 == '2':
        fam = input('Введите фамилию: ')
        found_contact = False
        for contact in contacts:
            if fam in contact[0]:
                print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер: {contact[3]}, Текст: {contact[4]}")
                found_contact = True
        if not found_contact:
            print('Контакт не найден.')

def main():
    try:
        contacts = read_contacts()
        running = True
        while running:
            comm = input('Введите команду (1 - добавить, 2 - просмотреть все, 3 - поиск, 4 - удалить, 5 - редактировать, 6 - выход): ')
            if comm == '1':
                add_contact(contacts)
                write_contacts(contacts)
            elif comm == '2':
                for contact in contacts:
                    print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер: {contact[3]}, Текст: {contact[4]}")
            elif comm == '3':
                search_contact(contacts)
            elif comm == '4':
                contacts = delete_contact(contacts)
                write_contacts(contacts)
            elif comm == '5':
                edit_contact(contacts)
                write_contacts(contacts)
            elif comm == '6':
                print('Программа завершена.')
                running = False
            else:
                print('Некорректная команда.')
    except FileNotFoundError:
        print('Файл не найден.')
    finally:
        contacts = []
        write_contacts(contacts)
        main()

if __name__ == '__main__':
    main()
