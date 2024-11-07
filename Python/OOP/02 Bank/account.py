class account:

    # Konstruktor (ctor)
    def __init__(self, owner:str, balance:float, iban:str, overdraw:bool=False):
        self.__owner = owner
        self.__balance = balance
        self.__iban = iban
        self.__overdraw = overdraw

    # getter
    def getOwner(self) -> str:
        return self.__owner

    def getBalance(self) -> float:
        return self.__balance
    
    def getIban(self) -> str:
        return self.__iban
    
    # setter
    def setOwner(self, value:str) -> None:
        self.__owner = value

    # Methoden
    def deposit(self, amount:float) -> None:
        if amount < 0:
            print("Betrag darf nicht negativ sein.")
        else:
            self.__balance = self.__balance + amount
    
    def withdraw(self, amount:float) -> None:
        if amount < 0:
            print("Betrag darf nicht negativ sein.")
        else:
            # Überprüfe ob zu wenig Geld am Konto
            if self.__balance < amount and self.__overdraw == False:
                print("Ihr Konto weist nicht genug Kapital auf.")
            else:
                self.__balance = self.__balance - amount
                print(f"Es wurden {amount} € vom Konto {self.__iban} abgehoben.")

    def __str__(self):
        return f"Owner: {self.__owner} \nIBAN: {self.__iban} \nBalance: {self.__balance}"
