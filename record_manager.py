import file_manager

def add_record(filename):
    """ Добавление новой записи. """
    date = input("Введите дату (гггг-мм-дд): ")
    category = input("Введите категорию (Доход/Расход): ")
    amount = float(input("Введите сумму: "))
    description = input("Введите описание: ")
    new_record = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    records = file_manager.load_records(filename)
    records.append(new_record)
    file_manager.save_records(records, filename)
    print("Запись добавлена.")

def edit_record(filename):
    """ Редактирование существующей записи. """
    records = file_manager.load_records(filename)
    for index, record in enumerate(records):
        print(f"{index + 1}: {record['date']} - {record['category']} - {record['amount']} - {record['description']}")
    record_number = int(input("Введите номер записи для редактирования: ")) - 1
    if 0 <= record_number < len(records):
        record = records[record_number]
        record['date'] = input(f"Введите новую дату ({record['date']}): ") or record['date']
        record['category'] = input(f"Введите новую категорию ({record['category']}): ") or record['category']
        record['amount'] = float(input(f"Введите новую сумму ({record['amount']}): ") or record['amount'])
        record['description'] = input(f"Введите новое описание ({record['description']}): ") or record['description']
        file_manager.save_records(records, filename)
        print("Запись обновлена.")
    else:
        print("Неверный номер записи.")
