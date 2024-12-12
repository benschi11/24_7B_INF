from __future__ import annotations
from typing import TYPE_CHECKING

from account import account

if TYPE_CHECKING:
    from bank import bank


class fileRepository:
    """
    Saves and loads objects from and to a file
    """
    def loadAccountsForBank(self, bankname:str) -> list[account]:
        filename = bankname.lower().replace(" ", "_") + "_accounts.csv"
        path = f"data/{filename}" # works only on Windows

        # öffne Datei
        datafile = open(path,"r", encoding="utf-8")

        firstLine = True

        accounts:list[account] = []

        for line in datafile:
            if firstLine == True:
                firstLine = False
                continue
            
            line = line.replace("\n","") # ersetze Zeilenumbruch
            # Spalte Zeile auf
            data = line.split(";")
            # Erstelle Objekt von Account
            a = account(data[0],float(data[1]),data[2],bool(data[3]))

            # zur Liste hinzufügen
            accounts.append(a)

        datafile.close()

        return accounts


    def saveAccountsForBank(self, Bank:bank):
        filename = Bank.getName().lower().replace(" ", "_") + "_accounts.csv"
        path = f"data/{filename}" # works only on Windows

        # öffne Datei
        datafile = open(path,"w", encoding="utf-8")

        datafile.write("owner;balance;iban;overdraw\n") # erste Zeile

        for a in Bank.getAccounts():
            line = f"{a.getOwner()};{a.getBalance()};{a.getIban()};{a.getOverdraw()}\n"
            datafile.write(line)


        # schließt Datei
        datafile.close()