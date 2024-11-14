from account import account
from bank import bank

raika = bank("Raiffeisenbank Weiz-Anger")
raika.loadAccounts()

# Account mit IBAN AT23123234549878 auslesen
a1 = raika.getAccountByIban("AT23123234549878")

# AT78881992918777

raika.transfer("AT78881992918777", "AT23123234549878", 400)

# Account printen
print(a1)
