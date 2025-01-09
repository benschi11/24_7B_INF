from account import account
from fileRepository import fileRepository

class bank:

    def __init__(self, name:str):
        self.__name = name
        self.__accounts:list[account] = []

    def getAccounts(self):
        return self.__accounts
    
    def getName(self):
        return self.__name

    def loadAccounts(self) -> None:
        """ Loads all Accounts from this bank
        """
        repository = fileRepository()

        self.__accounts = repository.loadAccountsForBank(self.__name)

    def getAccountByIban(self, iban:str) -> account | None:
        """
        Returns an account with the given IBAN.
        None if the account is not found.
        """
        # Suche Account aus Liste
        for account in self.__accounts:
            if account.getIban() == iban:
                return account
        # wenn iban nicht gefunden
        return None
    
    def transfer(self, ibanFrom:str, ibanTo:str, amount:float):

        # finde Accounts durch IBAN (getAccountByIban)
        account_from = self.getAccountByIban(ibanFrom)
        account_to = self.getAccountByIban(ibanTo)

        # überprüfe ob beide Accounts vorhanden
        if account_from == None or account_to == None:
            print("Einer der beiden Accounts ist nicht vorhanden. \nTransfer abgebrochen.")
        else:
            # Betrag vom Account abziehen
            account_from.withdraw(amount)

            # Betrag zu anderem Account hinzufügen
            account_to.deposit(amount)

    def addAccount(self, Account:account):
        # Account zur Bankliste hinzufügen
        self.__accounts.append(Account)

        # speichere auf Festplatte
        fileRepo = fileRepository()
        fileRepo.saveAccountsForBank(self)

    def deleteAccount(self, iban:str):
        # erhalte Account Objekt
        a = self.getAccountByIban(iban)
        # lösche Account aus Liste
        if a != None:
            self.__accounts.remove(a)
            # speichere auf die Festplatte
            fileRepo = fileRepository()
            fileRepo.saveAccountsForBank(self)
        else:
            print(f"Der Account mit IBAN {iban} wurde nicht gefunden.")
        

    
    def __str__(self):
        output = f"Name: {self.__name}\n"
        output += "-"*20 + "\n"
        output += "Accounts:\n"
        output += "-"*10 + "\n"

        for a in self.__accounts:
            output += str(a)+"\n"
            output += "-- \n"

        return output

