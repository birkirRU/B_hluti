# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10. september>
# Verkefni: <Föll Vikudagur>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>



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


def dagar_man(nrman,ar=2001):
    if nrman==4 or nrman==6 or nrman==9 or nrman==11:
        return 30
    elif nrman==2 and hlaupaar(ar):
        return 29
    elif nrman==2:
        return 28
    else:
        return 31
    

def dagar_fra_arsbyrjun(dagur, man, ar):
    dagar = 0
    dagar += dagur
    for manudur in range(1, man):
        dagar += dagar_man(manudur, ar)
    return dagar


def dagar_ad_arsbyrjun(ar):
    dagar = 1
    fjoldi_ara = ar - 1900
    
    for i in range(fjoldi_ara):
        if hlaupaar(1900 + i):
            dagar+= 366
        else:
            dagar+=365
    
    return dagar

def heiti_dags(dagur, man, ar):
    fjoldi_daga = 0

    fjoldi_daga += dagar_ad_arsbyrjun(ar)
    fjoldi_daga += dagar_fra_arsbyrjun(dagur, man, ar)

    dagurnr = fjoldi_daga%7

    #dagar_list = ["Laugardagur", "Sunnudagur", "Mánudagur", "Þriðjudagur", "Miðvikudagur", "Fimmtudagur", "Föstudagur"]
    #return dagar_list[dagurnr]

    if dagurnr == 0:
        return "laugardagur"
    elif dagurnr == 1:
        return "sunnudagur"
    elif dagurnr == 2:
        return "mánudagur"
    elif dagurnr == 3:
        return "þriðjudagur"
    elif dagurnr == 4:
        return "miðvikudagur"
    elif dagurnr == 5:
        return "fimmtudagur"
    elif dagurnr == 6:
        return "föstudagur"

    # 31. des 1899 = Sunnudagur
    # 1. jan 1900 = Mánudagur
    



def main():
    dagur = int(input("Dagur:"))
    man = int(input("Mánuður:"))
    ar = int(input("Ár:"))
    print ("Það er",heiti_dags(dagur,man,ar))
main()
