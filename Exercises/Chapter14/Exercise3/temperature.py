class Temp:
    __fahrenheight: float
    __celsius: float

    def __init__(self, value, type):
        if type == 'f':
            self.__fahrenheight = value
            self.toCelsuis(value)
        if type == 'c':
            self.__celsius = value
            self.toFahrenheight(value)

    @property
    def fahrenheight(self):
        return self.__fahrenheight
    
    @fahrenheight.setter
    def fahrenheight(self, value):
        self.__fahrenheight = value

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        self.__celsius = value
        

    def toCelsuis(self, value):
        celsius = round(((value - 32) * 5/9), 2)
        self.celsius = celsius

    def toFahrenheight(self, value):
        fahrenheight = round((value * 9/5 + 32), 2)
        self.fahrenheight = fahrenheight
