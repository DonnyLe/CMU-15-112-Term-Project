class Car:
    def __init__(self, initialGal, distanceTraveled, speed, gasPrice):
        self.initialGal = initialGal
        self.distanceTraveled = distanceTraveled
        self.speed = speed
        self.gasPrice =gasPrice
    

car = Car(20, 200, 100,50)

print("This car has this many gallons:", car.initialGal , "\n", "This is how far the car goes:",car.distanceTraveled, "\n", "This is the speed of the car: ",car.speed, "\n","This is the time taken to drive this distance: ")