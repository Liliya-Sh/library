import unittest

from app import all_books, search_book, change_status, delete_book, add_book


class Testlibrary(unittest.TestCase):
    """Тесты на для проверки работы функций"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_book(self):
        """Тестируем функцию add_book(добавляем новую книгу)"""
        new_book = ('\nID: 4\n'
                    'Название: Один плюс один\n'
                    'Автор: Джоджо Мойес\n'
                    'Год издания: 2014\n'
                    'Статус: в наличии'
                    )

        actual_result = add_book('Один плюс один', 'Джоджо Мойес', '2014')
        self.assertEqual(actual_result, new_book)

    def test_all_books(self):
        """Тестируем функцию all_books(список всех книг)"""
        book_list = ('\nID: 1\n'
                     'Название: Шантарам\n'
                     'Автор: Грегори Дэвид Робертс\n'
                     'Год издания: 2003\n'
                     'Статус: в наличии'
                     '\nID: 2\n'
                     'Название: Есть, молиться, любить\n'
                     'Автор: Элизабет Гилберт\n'
                     'Год издания: 2022\n'
                     'Статус: в наличии'
                     '\nID: 3\n'
                     'Название: Серебристая бухта\n'
                     'Автор: Джоджо Мойес\n'
                     'Год издания: 2007\n'
                     'Статус: в наличии'
                     '\nID: 4\n'
                     'Название: Один плюс один\n'
                     'Автор: Джоджо Мойес\n'
                     'Год издания: 2014\n'
                     'Статус: в наличии'
                     )

        actual_result = all_books()

        self.assertEqual(actual_result, book_list)

    def test_change_status(self):
        """Тестируем функцию change_status(меняется ли статус книги на 'выдана' или 'в наличии')"""
        status = 'У книги id:1, статус:выдана'

        actual_result = change_status(1, 'выдана')
        self.assertEqual(actual_result, status)

    def test_delete_book(self):
        """Тестируем функцию delete_book(удаляет книгу по id)"""
        del_book = 'Книга с id 3 была удалена.'

        actual_result = delete_book(3)
        self.assertEqual(actual_result, del_book)

    def test_search_book_author(self):
        """Тестируем функцию search_book(поиск книги по автору)"""
        book = ('\nID: 2\n'
                  'Название: Есть, молиться, любить\n'
                  'Автор: Элизабет Гилберт\n'
                  'Год издания: 2022\n'
                  'Статус: в наличии')

        actual_result = search_book(2, 'Элизабет Гилберт')
        self.assertEqual(actual_result, book)

    def test_search_book_title(self):
        """Тестируем функцию search_book(поиск книги по названию)"""
        book = ('Книги с такими данными нет')

        actual_result = search_book(1, 'Серебристая бухта')
        self.assertEqual(actual_result, book)

    def test_search_book_year(self):
        """Тестируем функцию search_book(поиск книги по году)"""
        book = ('\nID: 2\n'
                  'Название: Есть, молиться, любить\n'
                  'Автор: Элизабет Гилберт\n'
                  'Год издания: 2022\n'
                  'Статус: в наличии')

        actual_result = search_book(3, '2022')
        self.assertEqual(actual_result, book)


if __name__ == '__main__':
    unittest.main()
