from account import account

class bank:

    def __init__(self, name:str):
        self.__name = name
        self.__accounts = []

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
