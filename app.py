import json

from model import Book

filename = 'books_library.json'


def all_books():
    """Просмотреть список всех книг"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    books_list = []
    for txt in data['books']:
        book_info = Book(txt['id'], txt['title'], txt['author'], txt['year'], txt['status'])
        books_list.append(book_info.print_book_info())

    return ''.join(books_list)


def search_book(criterion, meaning):
    """Поиск книги по названию, автору или году"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    result = []
    for txt in data['books']:
        book_info = Book(txt['id'], txt['title'], txt['author'], txt['year'], txt['status'])
        if criterion == 'название' and txt['title'] == meaning:
            result.append(book_info.print_book_info())
        elif criterion == 'автор' and txt['author'] == meaning:
            result.append(book_info.print_book_info())
        elif criterion == 'год' and txt['year'] == int(meaning):
            result.append(book_info.print_book_info())
    if result:
        return ''.join(result)
    else:
        return "Книги с такими данными нет"


def change_status(id, status):
    """Меняем статус книги на 'выдана' или 'в наличии'"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for txt in data['books']:
        if txt['id'] == id:
            txt['status'] = status
            with open(filename, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=2)
            return f'У книги id:{id}, статус:{status}'

    return 'Книга с таким id не найдена.'


def add_book(title, author, year):
    """Добавить новую книгу"""
    try:
        year = int(year)
    except ValueError:
        return 'Введен неверный формат год издания'

    if len(title) < 2:
        return 'Слишком короткое название книги'
    elif len(author) < 2:
        return 'Слишком короткое имя автора'

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for txt in data['books']:
        if txt['title'] == title:
            return 'Такая книга уже есть в списке'

    id = len(data['books']) + 1

    new_book = Book(id, title, author, year, 'в наличии')
    data['books'].append(dict(id=id, title=title, author=author, year=year, status='в наличии'))

    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)

    return new_book.print_book_info()


def delete_book(id: int):
    """Удалить книгу по id"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for index, txt in enumerate(data['books']):
            if txt['id'] == id:
                data['books'].pop(index)
                with open(filename, 'w', encoding='utf-8') as out:
                    json.dump(data, out, ensure_ascii=False, indent=2)
                return f'Книга с id {id} была удалена.'

        return f'Книга с id {id} не найдена.'
