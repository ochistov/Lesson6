import time #импорт модуля, содержащего функцию sleep()

'''
Creation of the TrafficLight class with one color attribute, which is a 
dictionary containing the color and the time in seconds allocated for it. 
Creation of a method that provides alternate switching of traffic signals. 
To control the order of switching signals, a list with colors is used; 
the enumeration of colors is performed using the counter i. 
-----------------------------------------------------------------------------
Создание класса TrafficLight, имеющего один атрибут color, являющийся словарём, 
содержащим цвет и время в секундах, отведённое на него. Создание метода, 
обеспечивающего поочерёдное переключение сигналов светофора. Для контроля 
порядка переключения сигналов используется список с цветами, перебор цветов 
происходит с помощью счётчика i.
'''
class Trafficlight:
    __color = {'red' : 7, 'yellow' : 2, 'green' : 6}
  
    def running(self):
        i = 0 
        colors =[]
        for i in self.__color.keys():
            colors.append(i)
        
        while True:
            for i in range(len(self.__color)):
                now_color = colors[i]
                print(f"Now traffic light is {now_color}")
                time.sleep(int(self.__color[now_color]))
                if i > 2:
                    i = 0
                    continue
                continue
            continue

'''
Instantiating a class and calling a method 
-------------------------------------------------------------------------------
Создание экземпляра класса и вызов метода
'''
tl = Trafficlight()
tl.running()