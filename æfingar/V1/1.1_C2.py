# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <3. september>
# Verkefni: <Fjöldi sérhljóða í textastreng>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>


def fjoldiSerhljoda(text): 
    serhljodar = ["a",'á','e','é','i','í','o','ó','u','ú','y','ý','æ','ö']
    fjoldi = 0
    for serhljodi in serhljodar:
        fjoldi+=text.count(serhljodi)
        fjoldi+=text.count(serhljodi.upper())
    return fjoldi

def main():
    texti = input("Textastrengur: ")
    fjoldi = fjoldiSerhljoda(texti)
    print ("Það eru",fjoldi,"sérhljóðar í þessum texta")
main()


