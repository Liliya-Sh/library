from app import delete_book, all_books, change_status, search_book, add_book


def select_action():
    """Выберать действие"""
    try:
        while True:
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
                criterion = input("Введите критерий по которому будите искать книгу(название,автор,год): ")
                meaning = input("Введите значение: ")
                print(search_book(criterion, meaning))
            elif choice == 3:
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год публикации: ")
                print("Книга добавлена", add_book(title, author, year))
            elif choice == 4:
                id_book = int(input("Введите ID книги, у которой хотите поменять статус:"))
                status = input("Укажите какой у книги статус(в наличии/выдана):")
                print(change_status(id_book, status))
            elif choice == 5:
                id_book = int(input("Введите ID книги, которую хотите удалить:"))
                print(delete_book(id_book))
            elif choice == 6:
                break
            else:
                print("Указано не верное значение")
    except ValueError:
        print("Указано не верное значение")


if __name__ == '__main__':
    select_action()
