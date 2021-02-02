'''
Create parent class Car and child classes. Creation of methods in the parent 
class that describe the movement of the car. Change in the child 
classes of the method that displays the current car speed 
------------------------------------------------------------------------------
Создание родительского класса Car и дочерних классов. Создание в родительском 
классе методов, описывающих движение автомобиля. Изменение в дочерних 
классах метода, выводящего на экран текущую скорость автомобиля
'''
class Car:
    speed = float(input("Insert speed of car: "))
    color = input("Insert color of car: ")
    name = input("Insert name of car: ")
    is_police = bool(input("Type anything if car is police, leave empty if no: "))
    
    def start(self):
        print(f"Engine of {self.color} {self.name.title()} started")

    def go(self):
        print(f"{self.color.title()} {self.name.title()} go forward")
    
    def stop(self):
        print(f"{self.color.title()} {self.name.title()} stopped")
        
    def turn(self, direction):
        print(f"{self.color.title()} {self.name.title()} turned {direction}")
        
    def show_speed(self):
        print(f"Current speed of {self.color.title()} {self.name.title()} is {self.speed} km/h")

class TownCar(Car):
    speed = float(input("Insert speed of town car: "))
    color = "black"
    name = "mercedes-benz"
    is_police = False
    
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color.title()} {self.name.title()} exceeded speed by {self.speed - 60} km/h. Speed of {self.color} {self.name.title()} is {self.speed} km/h, speed limit is 60 km/h.")
        else:
            print(f"Current speed of {self.color.title()} {self.name.title()} is {self.speed}")

class SportCar(Car):
    speed = float(input("Insert speed of sport car: "))
    color = "blue"
    name = "lamborghini"
    is_police = False


class WorkCar(Car):
    speed = float(input("Insert speed of work car: "))
    color = "yellow"
    name = "bobcat"
    is_police = False
    
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color.title()} {self.name.title()} exceeded speed by {self.speed - 40} km/h. Speed of {self.color} {self.name.title()} is {self.speed} km/h, speed limit is 40 km/h.")
        else:
            print(f"Current speed of {self.color.title()} {self.name.title()} is {self.speed}")

class PoliceCar(Car):
    speed = float(input("Insert speed of police car: "))
    color = "police"
    name = "ford"
    is_police = True
    
'''
Instantiating a class and calling methods 
-------------------------------------------------------------------------------
Создание экземпляра класса и вызов методов
'''

####################
c = Car()
tc = TownCar()
sc = SportCar()
wc = WorkCar()
pc = PoliceCar()
####################
c.start()
tc.start()
sc.start()
wc.start()
pc.start()
####################
c.go()
tc.go()
sc.go()
wc.go()
pc.go()
####################
c.show_speed()
tc.show_speed()
sc.show_speed()
wc.show_speed()
pc.show_speed()
####################
c.stop()
tc.stop()
sc.stop()
wc.stop()
pc.stop()
####################
c.turn("left")
tc.turn("left")
sc.turn("left")
wc.turn("left")
pc.turn("left")
####################
c.turn("right")
tc.turn("right")
sc.turn("right")
wc.turn("right")
pc.turn("right")