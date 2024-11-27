# Birkir Snær Axelsson

input_file = input("Nafn textaskrár: ")

info = open(input_file, "r")

all_numbers = []

for line in info:
    number = int(line.strip())
    all_numbers.append(number)

length = len(all_numbers)
sum = sum(all_numbers)

print("Meðaltal talnanna er: {}".format( sum / length))
print("Hæsta talan er: {}".format(max(all_numbers)))