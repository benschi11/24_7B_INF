from account import account


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

        for line in datafile:
            if firstLine == True:
                firstLine = False
                continue
            
            line = line.replace("\n","") # ersetze Zeilenumbruch
            # Spalte Zeile auf
            data = line.split(";")
            # Erstelle Objekt von Account
            a = account(data[0],float(data[1]),data[2],bool(data[3]))

            print(line)

        datafile.close()


    def saveAccountsForBank(self, bankname:str):
        pass