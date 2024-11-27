# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <8. oktober>
# Verkefni: <Fallið is_Float>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>



def is_float(string_to_test):
    try:
        float(string_to_test)
        return True
    except ValueError:
        return False


def main():
    string_to_test = input("Sláðu inn float tölu: ")
    if is_float(string_to_test):
        print("ok slóst inn tölu")
    else:
        print("það á að slá inn tölu")
main()