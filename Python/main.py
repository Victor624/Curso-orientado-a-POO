from car import Car

if __name__ == "__main__":
    
    car = Car()
    car.license ="ams 235 "
    car.driver = "joaquin Villalba "
    print(vars(car))

    car2 = Car()
    car2.license = "252 kbs"
    car2.driver = "Esteban Garcia"
    print(vars(car2))