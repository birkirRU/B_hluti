
# Birkir Snær Axelsson

class Nemandi:
    def __init__(self, nafn, kennitala):
        self.name = nafn
        self.id = kennitala
    
    def __str__(self):
        return(f"Nafn nemanda: {self.name} Kennitala: {self.id}")


class Afangi:
    def __init__(self, nafn, maxfjoldi) -> None:
        self.name = nafn
        self.maxsize = maxfjoldi
        self.nemendur = []

    def __str__(self):
        final_string = ""
        name_string = f"Nafn námskeiðs: {self.name} Hámarksfjöldi: {self.maxsize}\n"
        final_string += name_string
        for student in self.nemendur:
            student_string = f"{student.__str__()}\n"
            final_string += student_string

        return final_string
        

    def skra_nemanda(self, nemandi):
        if len(self.nemendur) != self.maxsize:
            self.nemendur.append(nemandi)
    
    def hamark(self, new_maxfjoldi):
        self.maxsize = new_maxfjoldi
    

def main():
    jon = Nemandi("Jón Jónsson", "011299-3459") 
    erla = Nemandi("Erla Pétursdóttir", "221101-2220")
    gunnar = Nemandi("Gunnar Jónsson", "011101-2220")
    

    forritun = Afangi("Forritun", 60)
    forritun.skra_nemanda(jon)
    forritun.skra_nemanda(erla)
    forritun.hamark(2)
    forritun.skra_nemanda(gunnar)
    print(forritun)

main()