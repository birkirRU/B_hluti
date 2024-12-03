
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
        self.einkunnir = []

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
            self.einkunnir.append(-1)
    
    def hamark(self, new_maxfjoldi):
        self.maxsize = new_maxfjoldi

        if new_maxfjoldi < len(self.nemendur): # hægt að gera betur með del skipun, partition listan 
            for i in range(len(self.nemendur) - new_maxfjoldi):
                self.einkunnir.pop()
                self.nemendur.pop()
    
    def skra_einkunn(self, student_id, einkunn):
        for i, student in enumerate(self.nemendur):
            if student.id == student_id:
                self.einkunnir[i] = einkunn
    
    def medaleinkunn(self):
        einkun_list = []
        for einkunn in self.einkunnir:
            einkun_list.append(einkunn) if einkunn != -1 else False
        return f"Meðaleinkunn er: {sum(einkun_list)/(len(einkun_list))}"
        
    

def main():
    jon = Nemandi("Jón Jónsson", "011299-3459") 
    erla = Nemandi("Erla Pétursdóttir", "221101-2220")
    gunnar = Nemandi("Gunnar Jónsson", "011101-2220")
    

    forritun = Afangi("Forritun", 60)
    forritun.skra_nemanda(jon)
    forritun.skra_nemanda(erla)
    forritun.hamark(2)
    forritun.skra_nemanda(gunnar)

    forritun.skra_einkunn("011299-3459", 8) # skra einkunn jons
    forritun.skra_einkunn("221101-2220", 2) # skra einkunn erlu
    forritun.skra_einkunn("011101-2220", 10) # nær ekki að skrá einkunn, hamark = 2
    print(forritun.medaleinkunn())
    print()

    forritun.hamark(3)
    forritun.skra_nemanda(gunnar)
    forritun.skra_einkunn("011101-2220", 10) # skra einkunn gunnars
    forritun.skra_einkunn("221101-2220", 9) # endurskra einkunn erlu
    print(forritun.medaleinkunn())
    print()
    forritun.hamark(2) # fjarlæga gunnar
    
    print(forritun)
    print(forritun.medaleinkunn())

main()