# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10. september>
# Verkefni: <Dagar frá ársbyrjun>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>

def dagar_man(nrman,ar=2001):
    if nrman==4 or nrman==6 or nrman==9 or nrman==11:
        return 30
    elif nrman==2 and hlaupaar(ar):
        return 29
    elif nrman==2:
        return 28
    else:
        return 31
    
def hlaupaar(ar):
    if ar%4==0:
        hlar=True
    else:
        hlar=False
    if ar%100==0:
        hlar=False
    if ar%400==0:
        hlar=True
    return hlar

def dagar_fra_arsbyrjun(dagur, man, ar):
    dagar = 0
    dagar += dagur
    for manudur in range(1, man):
        dagar += dagar_man(manudur, ar)
    return dagar
    

def main():
    dagur = int(input("Dagur:"))
    man = int(input("Mánuður:"))
    ar = int(input("Ár:"))
    fjoldi_daga = dagar_fra_arsbyrjun(dagur,man,ar)
    print ("Fjöldi daga frá áramótum er:", fjoldi_daga)
main()


