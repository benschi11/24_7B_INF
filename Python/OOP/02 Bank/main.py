from account import account
from bank import bank
import random
from time import *

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

def deleteAccount(Bank:bank) -> None:
    print("Welches Konto möchten Sie löschen?")
    iban = input("IBAN: ")

    Bank.deleteAccount(iban)

    print("Account erfolgreich gelöscht!")

def transfer(Bank):
    

while True:
    print("Was möchten Sie tun:")
    print("(1) Accounts anzeigen")
    print("(2) Account hinzufügen")
    print("(3) Account löschen")
    print("(4) Überweisung tätigen")
    print("(q) Beendet das Programm")
    user_input = input(">")

    match user_input.strip():
        case "1":
            displayAccounts(Bank)
        case "2":
            createAccount(Bank)
        case "3":
            deleteAccount(Bank)
        case "4":
            transfer(Bank)
        case "q":
            break
        case _:
            print("Ihre Eingabe war wähhhhh!")
    
    sleep(2)
