class Product:
    # COD. ARTIC.	NOMBRE	STOCK	LISTA 1	LISTA 2	LISTA 3	LISTA 4	CATEGORIA
    __codArtic = None
    __name = None
    __stock = None
    __price1 = None
    __price2 = None
    __price3 = None
    __price4 = None
    __category = None

    def __init__(self, cod, name, stock, list1, list2, list3, list4, category):
        self.__codArtic = cod
        self.__name = name
        self.__stock = stock
        self.__price1 = list1
        self.__price2 = list2
        self.__price3 = list3
        self.__price4 = list4
        self.__category = category
        
    # Getters
    def getCodArtic(self):
        return self.__codArtic

    def getName(self):
        return self.__name

    def getStock(self):
        return self.__stock

    def getPrice1(self):
        return self.__price1

    def getPrice2(self):
        return self.__price2

    def getPrice3(self):
        return self.__price3

    def getPrice4(self):
        return self.__price4

    def getCategory(self):
        return self.__category

    # Setters
    def setCodArtic(self, cod):
        self.__codArtic = cod

    def setName(self, name):
        self.__name = name

    def setStock(self, stock):
        self.__stock = stock

    def setPrice1(self, price1):
        self.__price1 = price1

    def setPrice2(self, price2):
        self.__price2 = price2

    def setPrice3(self, price3):
        self.__price3 = price3

    def setPrice4(self, price4):
        self.__price4 = price4

    def setCategory(self, category):
        self.__category = category
