def get_title():
    """Запрашивает название книги и проверяет его корректность."""
    while True:
        title = input("Введите название книги: ").strip()
        if len(title) < 2:
            print('Слишком короткое название книги. Пожалуйста, введите название длиной не менее 2 символов.')
        else:
            return title


def get_author():
    """Запрашивает имя автора и проверяет его корректность."""
    while True:
        author = input("Введите автора книги: ").strip()
        if len(author) < 2:
            print('Слишком короткое имя автора. Пожалуйста, введите имя длиной не менее 2 символов.')
        else:
            return author


def get_year():
    """Запрашивает год публикации и проверяет его корректность."""
    while True:
        try:
            year = int(input("Введите год публикации: "))
            return year
        except ValueError:
            print('Введен неверный формат года издания. Пожалуйста, введите целое число.')


def get_id():
    """Запрашивает id и проверяет его корректность."""
    while True:
        try:
            id = int(input("Введите ID книги: "))
            if id == None:
                print('ID не может быть пустым значением.')
            else:
                return id
        except ValueError:
            print('Введен неверный формат ID. Пожалуйста, введите целое число.')


def get_status():
    """Запрашивает статус книги и проверяет его корректность."""
    while True:
        try:
            status = int(input("Укажите какой статус присвоить книге(в наличии - 1, выдана - 2):"))
            if status == 1:
                status_book = 'в наличии'
                return status_book
            elif status == 2:
                status_book = 'выдана'
                return status_book
            else:
                print('ID не может быть пустым значением. Укажите 1 или 2.')
        except ValueError:
            print('Введен неверный формат ID. Укажите 1 или 2.')


def get_criterion():
    """Запрашивает критерий, по которому необходимо искать книгу и проверяет его корректность."""
    while True:
        try:
            criterion = int(
                input("Введите критерий по которому будите искать книгу (название - 1, автор - 2, год - 3): "))
            if criterion == 1 or criterion == 2 or criterion == 3:
                return criterion
            else:
                print('Необходимо выбрать из представленных критериев. Укажите 1, 2 или 3.')
        except ValueError:
            print('Введен неверный формат критерия. Укажите 1, 2 или 3.')
