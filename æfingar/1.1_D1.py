# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <3. september>
# Verkefni: <skráar vinnsla>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>


def r_data(file_name):
    return open(file_name, "r", encoding='utf-8')


def print_data(text):
    for line in text:
        line = line.strip()
        print(line)

def main():
    file_name = input('Nafn textaskrár: ')
    file_text = r_data(file_name)
    print_data(file_text)

main()


# EFTIR AÐ SKILA OG KLÁRA