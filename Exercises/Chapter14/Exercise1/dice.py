import random
from dataclasses import dataclass

@dataclass
class Die:
    __value:int = 1

    @property
    def value(self):
        return self.__value
    
    @property
    def image(self):
        if self.__value == 1:
            print( " _____ \n" + \
                   "|     |\n" + \
                   "|  o  |\n" + \
                   "|_____|")
        if self.__value == 2:
            print( " _____ \n" + \
                   "|o    |\n" + \
                   "|     |\n" + \
                   "|____o|")
        if self.__value == 3:
            print(  " _____ \n" + \
                    "|o    |\n" + \
                    "|  o  |\n" + \
                    "|____o|") 
        if self.__value == 4:
            print(  " _____ \n" + \
                    "|o   o|\n" + \
                    "|     |\n" + \
                    "|o___o|") 
        if self.__value == 5:
            print(  " _____ \n" + \
                    "|o   o|\n" + \
                    "|  o  |\n" + \
                    "|o___o|")   
        if self.__value == 6:
            print(  " _____ \n" + \
                    "|o   o|\n" + \
                    "|o   o|\n" + \
                    "|o___o|")   
        
    @value.setter
    def value(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value can't be less than 1.")
        else:
            self.__value = value
                
    def roll(self) -> int:
        self.__value = random.randrange(1, 7)
        return self.__value
    
    def _post_int_(self):
        self.__value = self.roll()

                
class Dice:
    # use explicit initializer because @dataclass doesn't allow
    # attributes with a default value that's mutable (like list)

    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)

    def getTotal(self) -> int:
        count = 0
        for die in self.__list:
            count += die.value
        return count
    
    @property
    def list(self):
        return tuple(self.__list)
                
    def rollAll(self):
        for die in self.__list:
            die.roll()
