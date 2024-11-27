# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <8. oktober>
# Verkefni: <Lokaspurning A listar flugvélasæti>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það
# að vera tekið fram hér, einnig aðrar athugasemidir sem þú 
# vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða 
# annars aðila): <Já>

a_seat_rows = 7
seats = [[] for row in range(a_seat_rows)]
for r_i in range(a_seat_rows):
    for s_i in range(6):
        seats[r_i].append("Laust")

row_seats = ['A', 'B', 'C', 'D', 'E', 'F']


def ask_for_I():
    print("Veldu aðgerð:")
    print(" 1. Sýna stöðu sætabókana")
    print(" 2. Bóka sæti")
    print(" 3. Afbóka sæti")
    print(" 9. Hætta")
    val = int(input("Val: "))
    return val

def airplane_status():
    for row in range(a_seat_rows + 1):
        if row == 0:
            print(f"Sætaröð Sæti A\t{4*" "}B\t{4*" "}C\t{4*" "}D\t{4*" "}E\t{4*" "}F\t{4*" "}")
        else:
            print_row(row-1)
            

def print_row(r_i):
    print(f"{5*" "}{r_i+1}", end=" - ")
    for seat in seats[r_i]:
        print(f"{seat}", end="\t")
    print()

def book():
    print("Númer sætaraðar og sætis t.d. 2A")
    row_seat = input("Sláðu inn sæti: ")

    seat, row, seat_nr = get_seat_info(row_seat)

    if seats[row][seat_nr] == "Uppt.":
        print(f"Sæti {str(row+1)+str(seat)} er upptekið, þú getur ekki bókað það")
    else:
        seats[row][seat_nr] = "Uppt."
        print("Sæti hefur verið bókað")


def cancel():
    print("Númer sætaraðar og sætis t.d. 2A")
    row_seat = input("Sláðu inn sæti: ")

    seat, row, seat_nr = get_seat_info(row_seat)
    if seats[row][seat_nr] == "Laust":
        print(f"Sæti {str(row+1)+str(seat)} er laust, þú getur ekki afbókað það")
    else:
        seats[row][seat_nr] = "Laust"
        print("Sæti hefur verið afbókað")

def get_seat_info(row_seat):
    seat = row_seat[-1]
    return seat, int(row_seat[0:-1]) -1 , row_seats.index(seat)


def main():
    print(f"Fjöldi sætaraða: {a_seat_rows}")
    running = True
    while running:
        value = ask_for_I()
        print(f"{45*"-"}")
        if value == 1:
            airplane_status()
        elif value == 2:
            book()
        elif value == 3:
            cancel()
        elif value == 9:
            running = False
    

main()