'''
Creation of a class with attributes describing the worker. 
------------------------------------------------------------------------------
Создание класса с атрибутами, описывающими работника. 
'''
class Worker:
    name = input("Insert name: ")
    surname = input("Insert surname: ")
    position = input("Insert position: ")
    _income = {"wage" : float(input("Insert wage: ")), "bonus" : float(input("Insert bonus: "))}

'''
Создание дочернего класса, создание методов, обеспечивающих вывод на экран 
полного имени работника, полного дохода работника
------------------------------------------------------------------------------
Create a child class, create methods that displays the full name of the 
worker, the full income of the worker
'''
class Position(Worker):
    
    def get_full_name(self):
        print(f"Full name of worker is: {self.name} {self.surname}")
    
    def get_total_income(self):
        sum = 0
        for i, k in self._income.items():
            sum += k
        print(sum)

'''
Instantiating a class and calling methods 
-------------------------------------------------------------------------------
Создание экземпляра класса и вызов методов
'''

pos = Position()    
print(pos.name, pos.surname, pos.position, pos._income)
pos.get_full_name()
pos.get_total_income()