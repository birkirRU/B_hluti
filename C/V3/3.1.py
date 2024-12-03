# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/22/2024>
# Verkefni: <Æfingaverkefni A Farartæki>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>
class Vehicle:
    def __init__(self, brand, year) -> None:
        self.brand = brand 
        self.year = year
    
    def drive(self):
        print("I AM DRIVING")

    def display_info(self):
        print("Brand: " + f"{self.brand}")
        print("Year: " + f"{self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, fuel_type) -> None:
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"FuelType: {self.fuel_type}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_capacity) -> None:
        super().__init__(brand, year)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"engine_capacity: {self.engine_capacity}cc")


def main():
    vehicle = Vehicle("Generic Brand", 2020)
    vehicle.drive()
    vehicle.display_info()
    print()
    car = Car("Toyota", 2022, "Gasoline")
    car.drive()
    car.display_info()
    print()
    motorcycle = Motorcycle("Honda", 2021, 150)
    motorcycle.drive()
    motorcycle.display_info()

main()    