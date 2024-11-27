# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <3. september>
# Verkefni: <Rétt email>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>

def eremail(text):
    att_i = text.find('@')
    dot_i = text.find('.')
    if dot_i == -1 or att_i == -1:
        return False

    for char in text[0:att_i]:
        if char.isdigit() or char.isalpha():
            continue
        else:
            return False
    
    for char in text[att_i+1:dot_i]:
        if char.isdigit() or char.isalpha():
            continue
        else:
            return False
        
    if len(text[dot_i+1::]) ==2 or len(text[dot_i+1::]) ==3:
        for char in text[dot_i+1::]:
            if char.isalpha():
                continue
            else:
                return False
    else:
        return False

    return True



def main():
    texti = input("email: ")
    if eremail(texti):
        print(texti,'er rétt upp sett pósfang')
    else:
        print(texti,'er ekki rétt upp sett pósfang')
main()

