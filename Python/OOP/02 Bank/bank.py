from account import account

class bank:

    def __init__(self, name:str):
        self.__name = name
        self.__accounts:list[account] = []

    def loadAccounts(self) -> None:
        """ Loads all Accounts from this bank
        """
        # Lösche die aktuelle Liste
        self.__accounts.clear()

        # Account erstellen
        a1 = account("Benedikt Neuhold", 10000, "AT23123234549878",True)
        a2 = account("Rainer Zufall", 4000, "AT78881992918777")

        self.__accounts.append(a1)
        self.__accounts.append(a2)

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


