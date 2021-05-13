class Work:

    def __init__(self, title: str, owners):
        self.title = title
        self.owners = owners

    def __repr__(self):

        return f'Title: {self.title} , Owners: {self.owners}'




class Article(Work):

    def __init__(self, title: str, owners):
        super().__init__(title, owners)
        assert self.__is_valid(Researcher), "Only a researcher can write a ARTICLE!"

    def __is_valid(self, owners):
        if isinstance(self.owners, Researcher):
            x = True
        else:
            x = False
        return x

    def owners_number(self):
        if isinstance(self.owners, list):
            x = len(self.owners)
        else:
            x = 1
        return x

    def __repr__(self):
        return Work.__repr__(self)

class Poetry(Work):

    def __init__(self, title: str, owners):
        super().__init__(title, owners)
        assert self.__is_valid(Poet), "Only a poet can say a POETRY!"
        assert self.aouther(), "A poetry can not have multiple Poets!!!"

    def __is_valid(self, owners):
        if isinstance(self.owners, Poet):
            x = True
        else:
            x = False
        return x

    def aouther(self):
        if not isinstance(self.owners, list):
            x = True
        else:
            x = False
        return x

    def __repr__(self):
        return Work.__repr__(self)


class Book(Work):
    count: int = 0

    def __init__(self, title: str, owners, isbn: str):
        super().__init__(title, owners)
        self.isbn = isbn
        assert self.__is_valid(Writer), "Only a writer can write a BOOK!"


    def __is_valid(self, owners):
        if isinstance(self.owners, Writer):
            x = True
        else:
            x = False
        return x

    def owners_number(self):
        if isinstance(self.owners, list):
            x = len(self.owners)
        else:
            x = 1
        return x

    @classmethod
    def counting(cls):
        cls.count += 1


    def __repr__(self):
        return Work.__repr__(self)

class Man:

    def __init__(self, name: str, email: str = None, gender: str = None):
        self.name = name
        self.email = email
        self.gender = gender

    def __repr__(self):
        return self.name

class Researcher(Man):

    def __init__(self, name: str, field: str, email: str = None, gender: str = None):
        super().__init__(name, email, gender)
        self.field = field

class Writer(Man):

    def __init__(self, name: str, writing_code: int, email: str = None, gender: str = None):
        super().__init__(name, email, gender)
        self.writing_code = writing_code

class Poet(Man):

    def __init__(self, name: str, email: str = None, gender: str = None):
        super().__init__(name, email, gender)




researcher1 = Researcher('Hassan', "Art")
writer1 = Writer('Sam Ink', 12)
article1 = Article('first article', researcher1)
book1 = Book('Fantom', writer1, 'asdf-123')
poet1 = Poet('Hafez')
poet2 = Poet('Molana')
y = [poet1, poet2]
poetry1 = Poetry('big bang', poet2)
print(poetry1)
print(article1)