# Klasse "student"

class student:

    # Init Methode
    # wird beim Erstellen aufgerufen
    def __init__(self, firstname: str, lastname: str, schoolclass: str):
        # Werte in das Objekt speichern
        self.__firstname = firstname
        self.__lastname = lastname
        self.__schoolclass = schoolclass
    
    # Methoden
    # getter
    def getFirstname(self) -> str:
        return self.__firstname

    def getLastname(self) -> str:
        return self.__lastname
    
    def getSchoolClass(self) -> str:
        return self.__schoolclass
    
    #setter
    def setFirstname(self, value:str) -> None:
        if len(value) <= 1:
            # Fehler ausgeben
            raise Exception("Lenght of Firstname must greater than 1!")
        else:
            self.__firstname = value
    
    def setLastname(self, value:str) -> None:
        if len(value) <= 1:
            # Fehler ausgeben
            raise Exception("Lenght of Lastname must greater than 1!")
        else:
            self.__lastname = value
    
    def setSchoolClass(self, value:str) -> None:
        if len(value) <= 1:
            # Fehler ausgeben
            raise Exception("Lenght of SchoolClass must greater than 1!")
        else:
            self.__schoolclass = value


    def registerForCourse(self, courseName:str) -> None:
        print(f"{self.getFirstname()} {self.getLastname()} hat sich erfolgreich für den Kurs {courseName} angemeldet.")
    
    # Methode wenn zu str konvertiert wird
    def __str__(self):
        return f"{self.getLastname()} {self.getFirstname()} - {self.getSchoolClass()}"
