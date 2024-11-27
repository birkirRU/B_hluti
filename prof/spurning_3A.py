# Birkir Snær Axelsson

tala = int(input("Tala: "))

talna_listi = []

while tala != 0:
    talna_listi.append(tala)
    tala = int(input("Tala: "))


textaskra = input("Nafn textaskrár: ")

skra_inn = open(textaskra, "w")
for tala in talna_listi:
    print(tala, file=skra_inn)
print(f"Tölurnar voru vistaðar í skránni: {textaskra}")

print("Tölurnar í öfugri röð eru: ")

for tala in talna_listi[::-1]:
    print(tala)
skra_ut = open(textaskra, "r")















TABLE = [ # predefined table .
    [],
    [],
    [],
    [],
]

# listi sem geymir borðið, (nested list)

working_table = [ 
    [0, 0, 6, 9, 0, 5, 0, 1, 0], 
    [0, 0, 6, 9, 0, 5, 0, 1, 0], 
    [0, 0, 6, 9, 0, 5, 0, 1, 0], 
    [0, 0, 6, 9, 0, 5, 0, 1, 0], 
    [0, 0, 6, 9, 0, 5, 0, 1, 0], 
    [0, 0, 6, 9, 0, 5, 0, 1, 0], 
    [0, 0, 6, 9, 0, 5, 0, 1, 0], 
    [0, 0, 6, 9, 0, 5, 0, 1, 0], 
    [0, 0, 6, 9, 0, 5, 0, 1, 0]
    ]  


# Fall sem teiknar allt borðið

def display_tabel():
    print(working_table) # nested for loop til þess að teikna hana.
    for y in range(0,9):
        for x in range(0,9):
            pass
    pass


def is_in_row():
    pass

def is_in_column():
    pass

def is_in_box():
    pass

def is_same_table():
    pass

def save_table():
    skra = open("nafn_á_skrá.txt", "w") # w fyrir write

    # nota display_table function
    print("dotið sem er i display_table", file=skra) # til þess að skrifa í nafn_á_skrá.txt
    pass