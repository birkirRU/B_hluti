# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <29. ágúst>
# Verkefni: <Vikudagur>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>



def vikudagur(nrdags):
    if nrdags > 7 or nrdags < 1:
        return "Rangur innsláttur"
    elif nrdags == 1:
        return "Sunnudagur"
    elif nrdags == 2:
        return "Mánudagur"
    elif nrdags == 3:
        return "Þriðjudagur"
    elif nrdags == 4:
        return "Miðvikudagur"
    elif nrdags == 5:
        return "Fimmtudagur"
    elif nrdags == 6:
        return "Föstudagur"
    elif nrdags == 7:
        return "Laugardagur"


def main():
    nrdags = int(input("Númer dags: "))
    print(vikudagur(nrdags))

main()