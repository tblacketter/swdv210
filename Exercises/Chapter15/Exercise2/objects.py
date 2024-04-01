from dataclasses import dataclass

# must be coded before Book class, as Book class has an Authors type hint
# isn't a data class because has an attribute that's a list
class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    def __str__(self):
        temp = ""
        for author in self.__list:
            temp += str(author) + ", "
        temp = temp[:-2] 
        return temp
    
    def __iter__(self):
        for author in self.__list:
            yield author

    @property
    def count(self):
        return len(self.__list)
    
    
@dataclass
class Book:
    title:str = ""
    authors:Authors = None
    
    def __str__(self):
        return f"{self.title} by {self.authors}"
    
@dataclass
class Author:
    firstName:str = ""
    lastName:str = ""

    def __str__(self):
        return f"{self.firstName} {self.lastName}"




