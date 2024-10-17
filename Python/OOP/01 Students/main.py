from student import student
# from student import student

# Erstelle neue Instanz (Objekt) von student
s1 = student("Benedikt", "Neuhold", "7B")

# weiteres Objekt von student
s2 = student("Michi", "Hirt", "7B")

studentlist = [s1,s2]

# drittes Objekt
s3 = student("Mira", "Musterfrau","1A")
s2.registerForCourse("Programmieren 2")
studentlist.append(s3)

try:
    s3.setFirstname("Max")
except Exception as e:
    print(f"Fehler: {e}")


for s in studentlist:
    print(s)

