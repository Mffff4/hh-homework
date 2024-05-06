import record_manager
import reports

def main_menu():
    filename = 'data.txt'
    while True:
        print("\nГлавное меню:")
        print("1. Показать баланс")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск по записям")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            reports.show_balance(filename)
        elif choice == '2':
            record_manager.add_record(filename)
        elif choice == '3':
            record_manager.edit_record(filename)
        elif choice == '4':
            reports.search_records(filename)
        elif choice == '5':
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main_menu()
