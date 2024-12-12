from account import account
from bank import bank
import random

def displayAccounts(Bank:bank) -> None:
    for a in Bank.getAccounts():
        print(f"{a.getIban()} ({a.getOwner()})")

def generateNewIban(countryCode:str) -> str:
    iban = countryCode
    
    # 18 zufällige Zahlen erstellen
    for i in range(18):
        z = random.randint(0,9)
        iban += str(z)
    
    return iban



def createAccount(Bank:bank) -> account:
    print("-"*10)
    print("- Neues Konto hinzufügen.")
    print("-"*10)
    name = input("Name: ")
    overdraw_input = input("Darf der Benutzer überziehen? j/n")

    if overdraw_input == "j":
        overdraw = True
    else:
        overdraw = False
    
    iban = generateNewIban("AT")

    # neuen Account erstellen
    newAccount = account(name,0,iban,overdraw)
    Bank.addAccount(newAccount)


print("-"*20)
print("Banksystem 1.0")
print("-"*20)

while True:
    print("Welche Bank möchten Sie laden?")
    bankname = input(">")

    try:
        Bank = bank(bankname)
        Bank.loadAccounts()
        break
    except:
        print("Die Bank wurde leider nicht gefunden.")

print("Was möchten Sie tun:")
print("(1) Accounts anzeigen")
print("(2) Account hinzufügen")
print("(3) Account löschen")
print("(4) Überweisung tätigen")
user_input = input(">")

match user_input.strip():
    case "1":
        displayAccounts(Bank)
    case "2":
        createAccount(Bank)
