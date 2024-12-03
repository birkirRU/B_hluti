# Birkir Snær Axelsson


class Nemandi:
    def __init__(self, nafn, kennitala):
        self.name = nafn
        self.id = kennitala
    
    def __str__(self):
        return(f"Nafn: {self.name} Kennitala: {self.id} ")


def main():
    jon = Nemandi("Jón Jónsson", "011299-3459") 
    erla = Nemandi("Erla Pétursdóttir", "221101-2220")
    print(jon)

main()