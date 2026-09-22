
def sum():
    print("my sum")


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The vehicle {self.brand} starts.")

    def stop(self):
        print(f"The vehicle {self.brand} stops.")

class Car(Vehicle):
    def open_door(self):
        print("The door opens.")

class Bicycle(Vehicle):
    def do_ride(self):
        print("Ride!!")
    
    def stop(self):
        print(f"The bicyle stops.")
