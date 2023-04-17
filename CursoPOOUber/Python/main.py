from car import Car
from account import Account

if __name__ == "__main__": 
    print("Hola mundo") 

    car = Car("AMS234", Account("Andres Herrera", "JFD345"))
    print(vars(car))
    print(vars(car.drive))

    car2 = Car("ADF452", Account("Marta Ortiz", "HJF342"))

    # car = Car()
    # car.license = "AMS234"
    # car.driver = "Andres Herrera"
    # print(vars(car))

    # car2 = Car()
    # car2.license = "ADF452"
    # car2.drive = "Marta Ortiz"
    # print(vars(car2))