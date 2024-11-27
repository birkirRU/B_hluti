# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <29. ágúst>
# Verkefni: <Lesa einkunn>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>

def lesa_einkunn():
    einkun = float(input("Sláið inn einkunn á bilinu frá 0 til 10: "))
    if einkun < 0 or einkun > 10:
        print("einkun á að vera á bili 0 - 10")
        return lesa_einkunn()
    else:
        return einkun

def main():
    eink = lesa_einkunn()
    print("Þú slóst inn einkunnina", eink)

main()