# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <29. ágúst>
# Verkefni: <BMI Stuðull>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>


def bmi(h, t):
    return t / h**2

def main():
    haed = float(input("Hæð í metrum: "))
    thyngd = float(input("Þyngd í kg: "))
    print ("BMI: {:4.2f}".format(bmi(haed,thyngd)))
main()