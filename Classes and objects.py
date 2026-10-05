#
#This is to show declaring and using a  class
#
#

class FriendsList:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name

def list_name(self):
    return f'{self.name.upper()} {self.last_name.upper()}'

friend1 = FriendsList(name='Abel',last_name='Bogale')
friend2 = FriendsList(name='Yonas',last_name='Benebr')

print(list_name(friend1))
print(list_name(friend2))
class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)
####
#
#
#  getattr(), setattr(), hasattr(), delattr()
#

class CarList:
    def __init__(self,brand,model,year):
        self.Brand = brand
        self.Model = model
        self.Year = year
    def list_brand(self):
        return f'The car model is {car1.Model}  The car year is {car1.Year}  The car brand is {car2.Brand}'
car1 = CarList("Mercedes",'Eclass', 1999)
car2 = CarList("Mercedes",'sclass', 2999)
car3 = CarList("Mercedes",'Cclass', 3999)

print(car1.list_brand())

print(getattr(car1,'Brand'))
print(getattr(car2,'Brand'))

