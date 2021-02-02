'''
Creating a class, creating a method that calculates the mass of asphalt 
required to cover the roadway according to the specified parameters 
------------------------------------------------------------------------------
Создание класса, создание метода, с помощью которого рассчитывается 
масса асфальта, необходимого для покрытия дорожного полотна по указанным 
параметрам
'''
class Road:
    _length = 20
    _widgh = 5000
    
    def mass_asphalt(self,
                     mass1cm = int(input("Input mass for 1 m^2 of road: ")), 
                     thickcm = int(input("Input thick of road: "))):
        return int((self._length * self._widgh * mass1cm * thickcm ) / 1000)
    
'''
Instantiating a class and calling a method 
-------------------------------------------------------------------------------
Создание экземпляра класса и вызов метода
'''
r = Road()
print(int(r.mass_asphalt()))