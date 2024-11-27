# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <12. september>
# Verkefni: <Listar-röðunarnafn>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>

def rodunarnafn(nafn_splitted):
    
    fornafn = nafn_splitted.pop()
    nafn_splitted.insert(1, fornafn)
    
    return nafn_splitted


def main():
    nafn = input("Sláðu inn fullt nafn: ")
    nafn_splitted = nafn.split()
    if len(nafn_splitted) >=2 :
        radad_nafn = rodunarnafn(nafn_splitted)
        print('Röðunarnafn: ', end='')
        print(*radad_nafn)
    else:
        print("Það á að slá inn a.m.k. fornafn og eftirnafn")
main()

