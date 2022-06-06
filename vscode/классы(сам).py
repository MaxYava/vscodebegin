class Flat():
    """описание квартиры"""
    def __init__(self,number):
        """свойства квартиры""" 
        self.number = number 
    def заселение(self):
        """заселяет жильцов"""
        print("Жильцы в доме" + "под номером" + self.number + "получили квартиры")
F1 = Flat("3")
F2 = Flat(16) 
print(F1.number)    