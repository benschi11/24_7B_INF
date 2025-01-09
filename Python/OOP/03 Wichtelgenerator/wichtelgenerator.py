# 1) Namenseingabe per Console
# 2) Wichtelzuweisung generieren
#    - Person sich nicht selber zieht
#    - ein Name mehrmals gezogen wird
import random


print("#"*30)
print("# Wichtelgenerator 1.0")
print("#"*30)

names = []

def generate(names:list[str]) -> dict[str,str]:
    dictionary = dict() # leeres Dictionary

    # Kopie der Liste anlegen
    wichtel = names.copy()

    for name in names:
        w = random.choice(wichtel)

        if w == name and len(wichtel) == 1:
            return -1

        while w == name:
            w = random.choice(wichtel)
        
        dictionary[name] = w
        wichtel.remove(w)
    
    return dictionary

while True:
    user_input = input("Name eingeben oder 'x' für generieren: ")

    if user_input == "x":
        break

    names.append(user_input)

while True:
    d = generate(names)
    if d != -1:
        for key, value in d.items():
            print(f"{key} muss {value} beschenken.")
        

        break
    else:
        print("Letzte Person zieht sich selber - Restart")