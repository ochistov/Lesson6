'''
Create a parent Stationery class with a draw method and child classes 
Pen, Pencil, and Handle. Changing the draw method for each of the child classes 
------------------------------------------------------------------------------
Создание роодительского класса Stationery с методом draw и дочерних классов 
Pen, Pencil и Handle. Изменение метода draw для каждого из дочерних классов
'''
class Stationery:
    title = None
    def draw(self):
        print("Start drawing")
        
class Pen(Stationery):
    def draw(self):
        print("Start drawing with pen")

class Pencil(Stationery):
    def draw(self):
        print("Start drawing with pencil")

class Handle(Stationery):
    def draw(self):
        print("Start drawing with handle")
'''
Instantiating a class and calling methods 
-------------------------------------------------------------------------------
Создание экземпляра класса и вызов методов
'''
s = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

s.draw()
pen.draw()
pencil.draw()
handle.draw()