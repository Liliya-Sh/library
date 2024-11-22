class Book:
    """Модель Книги"""

    def __init__(self, id: int, title: str, author: str, year:int, status='в наличии'):
        """Инициализируем атрибуты"""
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def print_book_info(self):
        """Вывод информации о книге"""
        return (f"\nID: {self.id}\n"
                f"Название: {self.title}\n"
                f"Автор: {self.author}\n"
                f"Год издания: {self.year}\n"
                f"Статус: {self.status}")
