from account import account
from bank import bank

def displayAccounts(Bank:bank) -> None:
    for a in Bank.getAccounts():
        print(f"{a.getIban()} ({a.getOwner()})")

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
