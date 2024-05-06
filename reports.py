import file_manager

def show_balance(filename):
    """ Показать текущий баланс, доходы и расходы. """
    records = file_manager.load_records(filename)
    total_income = sum(record['amount'] for record in records if record['category'] == 'Доход')
    total_expense = sum(record['amount'] for record in records if record['category'] == 'Расход')
    print(f"Общий доход: {total_income}")
    print(f"Общий расход: {total_expense}")
    print(f"Текущий баланс: {total_income - total_expense}")

def search_records(filename):
    """ Поиск по записям. """
    search_query = input("Введите критерий поиска (дата, категория, сумма, описание): ")
    records = file_manager.load_records(filename)
    found_records = [record for record in records if search_query.lower() in str(record).lower()]
    for record in found_records:
        print(f"{record['date']} - {record['category']} - {record['amount']} - {record['description']}")
    if not found_records:
        print("Записи не найдены.")
