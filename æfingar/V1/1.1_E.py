# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10. september>
# Verkefni: <Talning daga>
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


def dagar_arsbyrjun(ar):
    dagar = 1
    fjoldi_ara = ar - 1900
    
    for i in range(fjoldi_ara):
        if hlaupaar(1900 + i):
            dagar+= 366
        else:
            dagar+=365
    
    return dagar



def main():
    ar = int(input("Ár:"))
    fjoldi_daga = dagar_arsbyrjun(ar)
    print ("Fjöldi daga frá 31.des 1899:",fjoldi_daga)
main()