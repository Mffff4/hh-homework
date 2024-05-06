def load_records(filename):
    """ Загрузка записей из файла. """
    records = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    date, category, amount, description = line.strip().split(',')
                    records.append({
                        'date': date,
                        'category': category,
                        'amount': float(amount),
                        'description': description
                    })
    except FileNotFoundError:
        print("Файл данных не найден, будет создан новый.")
    return records

def save_records(records, filename):
    """ Сохранение записей в файл. """
    with open(filename, 'w') as file:
        for record in records:
            file.write(f"{record['date']},{record['category']},{record['amount']},{record['description']}\n")

