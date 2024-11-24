from app import all_books, change_status, delete_book, add_book, search_book
from data_cquisition import get_id, get_status, get_year, get_author, get_title, \
    get_criterion


def select_action():
    """Выберать действие"""
    while True:
        try:
            print("\nВыберите действие:")
            print("1. Просмотреть список книг")
            print("2. Поиск книги")
            print("3. Добавить книгу")
            print("4. Поменять статус")
            print("5. Удалить книгу")
            print("6. Закрыть программу")

            choice = int(input("Введите номер действия (1/2/3/4/5/6): "))
            if choice == 1:
                print(all_books())

            elif choice == 2:
                criterion = get_criterion()
                if criterion == 1:
                    meaning = get_title()
                elif criterion == 2:
                    meaning = get_author()
                elif criterion == 3:
                    meaning = get_year()
                print(search_book(criterion, meaning))

            elif choice == 3:
                title = get_title()
                author = get_author()
                year = get_year()
                result = add_book(title, author, year)
                print("Книга добавлена:", result)

            elif choice == 4:
                id_book = get_id()
                status_book = get_status()
                print(change_status(id_book, status_book))

            elif choice == 5:
                id_book = get_id()
                print(delete_book(id_book))

            elif choice == 6:
                break
            else:
                print("Введите 1/2/3/4/5 или 6.")
        except ValueError:
            print("Введите 1/2/3/4/5 или 6.")


if __name__ == '__main__':
    select_action()
