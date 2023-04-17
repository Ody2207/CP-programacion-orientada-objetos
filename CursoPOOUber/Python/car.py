from account import Account
class Car:
    id          = int
    license     = str
    drive       = Account("","")
    passenger   = int
    
    def __init__(self, license, drive):
        self.license    = license
        self.drive      = drive