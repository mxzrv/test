class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year


    def __str__(self):
        return 'Автор: ' + self.author + ', Название: ' + self.name