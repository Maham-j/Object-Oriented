class Fruit:
    def __init__(self,name,uprice,uname,sucount,suname):
        # self, the object just constructed and in initiazilation 
        # name, name of the fruit, e.g. Kela, Amrood, etc
        # uprice, unit price of fruit
        # uname, unit name e.g. unit, piece, kg, meter, etc
        # sucount, count in sale unit, e.g., for dozen it is 12, for pack it may be 4,5 or 10, etc
        # suname, sale unit e.g. dozens, kgs, meters, etc
        
        self.__fruitname = name
        self.__unitprice = uprice
        self.__unitname = uname
        self.__countinsales = sucount
        self.__nameinsales = suname
        
    def __repr__(self):
        # self, the object to be represented at a sequence of bytes
        return f"{self.__fruitname} ==> price: {self.__unitprice} per {self.__unitname} saleable as {self.__nameinsales}s "

    def __str__(self):
        # self, the object to be represented at a sequence of characters
        return self.__repr__()
    
    def set_fruitname(self,name):
        self.__fruitname = name
    
    def get_fruitname(self):
        return self.__fruitname
    
    def set_unitprice(self,uprice):
        self.__unitprice = uprice
    
    def get_unitprice(self):
        return self.__unitprice
    
    def set_unitname(self,uname):
        self.__unitname = uname
    
    def get_unitname(self):
        return self.__unitname
    
    def set_countinsales(self,sucount):
        self.__countinsales = sucount
    
    def get_countinsales(self):
        return self.__countinsales
    
    def set_nameinsales(self,suname):
        self.__nameinsales = suname
    
    def get_nameinsales(self):
        return self.__nameinsales
    
    def payment(self, units):
        # self, the object under sale
        # units, how many units under the sale
        return units * self.__unitprice * self.__countinsales
    
    def __equi__(self, other):
        return (self.__fruitname == other.get_fruitname() and
                self.__unitprice == other.get_unitprice() and
                self.__unitname == other.get_unitname() and
                self.__countinsales == other.get_countinsales() and
                self.__nameinsales == other.get_nameinsales())

    def __nonqui__(self, other):
        return not self.__equi__(other)

def main():
    k = Fruit("Kela", 35, "unit",12,"dozen" )
    t = Fruit("Turbooz", 25, "kg", 1, "kg")
    m = Fruit("Strawberry", 15 , "Kg" , 2 , "kg")
    
    print('Avaliable Fruits')
    print(t)
    print(k)
    print(m)
    
    print(k.get_fruitname(), "of quantity 2.5 costs", k.payment(2.5))
    print(t.get_fruitname(), "of quantity 5 costs", t.payment(5))
    print(m.get_fruitname(), "of quantity 2 costs", t.payment(2))
    print(m.__equi__(k))
    print(k.__equi__(t))
    print(t.__equi__(m))
    print(m.__nonqui__(t))
    print(k.__nonqui__(m))
    print(t.__nonqui__(k))
    
main()
