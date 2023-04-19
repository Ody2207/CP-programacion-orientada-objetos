from car import Car
from account import Account
from uberBlack import UberBlack
from uberPool import UberPool

if __name__ == "__main__": 
    print("Hola mundo") 

    car = Car("AMS234", Account("Andres Herrera", "JFD345"))
    print(vars(car))
    print(vars(car.drive))

    uberBlack = UberBlack('JKF234', Account('Andres Herrera', 'BNF234'), 'Ferrari', 'No se modelos de ferrari xd')
    print(vars(uberBlack))

    uberPool = UberPool('JFL234', Account('Fernanda Segunda', 'FJK234'), 'Bocho2004')
    print(vars(uberPool))

    # car = Car()
    # car.license = "AMS234"
    # car.driver = "Andres Herrera"
    # print(vars(car))

    # car2 = Car()
    # car2.license = "ADF452"
    # car2.drive = "Marta Ortiz"
    # print(vars(car2))