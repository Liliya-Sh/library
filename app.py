import json

from model import Book

filename = 'books_library.json'


def open_file():
    """Открываем файл со списком книг.(books_library.json)"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Файл books_library.json не найден.")
        return None


def save_to_file(data):
    """Сохраняем данные в файл books_library.json"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def all_books():
    """Просмотреть список всех книг"""
    data = open_file()
    books_list = []
    for book in data['books']:
        book_info = Book(book['id'], book['title'], book['author'], book['year'], book['status'])
        books_list.append(book_info.print_book_info())

    return ''.join(books_list)


def search_book(criterion, meaning):
    """Поиск книги по названию, автору или году"""
    data = open_file()
    result = []
    for book in data['books']:
        book_info = Book(book['id'], book['title'], book['author'], book['year'], book['status'])
        if criterion == 1 and book['title'].lower() == meaning:
            result.append(book_info.print_book_info())
        elif criterion == 2 and book['author'] == meaning:
            result.append(book_info.print_book_info())
        elif criterion == 3 and book['year'] == int(meaning):
            result.append(book_info.print_book_info())
    if result:
        return ''.join(result)
    else:
        return "Книги с такими данными нет"


def add_book(title, author, year):
    """Добавить новую книгу"""
    data = open_file()

    for book in data['books']:
        if book['title'] == title:
            return 'Такая книга уже есть в списке'

    max_id = max(book['id'] for book in data['books']) if data else None
    id = max_id + 1

    new_book = Book(id, title, author, year, 'в наличии')
    data['books'].append(dict(id=id, title=title, author=author, year=year, status='в наличии'))

    save_to_file(data)

    return new_book.print_book_info()


def change_status(id, status_book):
    """Меняем статус книги на 'выдана' или 'в наличии'"""
    data = open_file()

    for book in data['books']:
        if book['id'] == id:
            book['status'] = status_book
            save_to_file(data)
            return f'У книги id:{id}, статус:{status_book}'

    return 'Книга с таким id не найдена.'


def delete_book(id: int):
    """Удалить книгу по id"""
    data = open_file()

    for index, txt in enumerate(data['books']):
        if txt['id'] == id:
            data['books'].pop(index)
            save_to_file(data)
            return f'Книга с id {id} была удалена.'

    return f'Книга с id {id} не найдена.'
