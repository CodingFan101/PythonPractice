class Car(object):
    def __init__(self, color, type):
        self.color = color
        self.type = type
    def setColor(self, color):
        self.color = color
    def setType(self, type):
        self.type = type
    def getColor(self):
        return self.color
    def getType(self):
        return self.type


class Vehicle(Car):
    def number_of_wheels(self):
        print("There are four wheels on most vehicles, including my dream one.")


dreamCar = Vehicle("Yellow", "Hyundai Elantra")
print(dreamCar.getColor())
print(dreamCar.getType())
dreamCar.setColor("Gray")
dreamCar.setType("Ford Focus")
print(dreamCar.getColor())
print(dreamCar.getType())
dreamCar.number_of_wheels()