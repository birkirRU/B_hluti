
# Birkir Snær Axelsson

f_starfsm = int(input("Hvað eru margir starfsmenn í hópnum: "))

kaup_listi = []
laun_starfsmanna = []

for starfsm in range(1, f_starfsm+1):
    tima_kaup = int(input(f"Skráið tímakaup starfsmanns nr {starfsm}: "))
    f_stunda= int(input(f"Skráið fjölda vinnustunda starfsmanns nr {starfsm}: "))

    kaup_listi.append([tima_kaup, f_stunda])

print("\nTímakaup og vinnustundir: ")
print("Starfsmaður  tímakaup og vinnustundir")

for i, starfsm in enumerate(kaup_listi):
    print(f"{i+1:<13}{starfsm[0]:<12}{starfsm[1]}")

print("\nLaun Starfsmanna: ")

for i, starfsm in enumerate(kaup_listi):
    sum_starfsm = starfsm[0] * starfsm[1]
    laun_starfsmanna.append(sum_starfsm)
    print(f"Starfsmaður {i+1} {sum_starfsm}")

print(f"Starfsmaður {laun_starfsmanna.index(max(laun_starfsmanna)) + 1} er með hæstu launin")
