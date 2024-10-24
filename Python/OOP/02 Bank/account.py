class account:

    # Konstruktor (ctor)
    def __init__(self, owner:str, balance:float, iban:str):
        self.__owner = owner
        self.__balance = balance
        self.__iban = iban

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
            self.__balance = self.__balance - amount

