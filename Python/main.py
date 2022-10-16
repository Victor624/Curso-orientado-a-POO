from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car("adabel","25252",Account("253535","kjbiubjk"))
   
    print(vars(car))
    print(vars(car.driver))

    