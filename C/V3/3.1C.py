# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/22/2024>
# Verkefni: <Employee>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>

class Person:
    def __init__(self, name, age ) -> None:
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, email, salary, department, position) -> None:
        super().__init__(name, age) 
        self.email = email
        self.salary = salary 
        self.department = department
        self.position = position

    def __str__(self):
        return f"Nafn: {self.name}, Aldur: {self.age}, Netfang: {self.email}, \nLaun: {self.salary}, Deild: {self.department}, Staða {self.position}"

    def give_raise(self, percentage):
        self.salary = round(self.salary*(1+percentage/100))

    def change_department(self, new_deparment):
        self.department = new_deparment

    def promote(self, new_postition):
        self.position = new_postition
    
    def add_overtime(self, hours):
        self.salary += hours*5000



def main():
    employee1 = Employee("Jón Jónsson", 34, "jon@jon.is", 400000, "Söludeild", "Sölumaður")
    print(employee1.salary)
    employee1.give_raise(10)
    print(employee1.salary)
    print(employee1.position)
    employee1.promote("Sölustjóri")
    print(employee1.position)
    employee1.change_department("Fjármálasvið")
    employee1.promote("Fjármálastjóri")
    employee1.add_overtime(12)
    print(employee1.salary)
    print(employee1)

main()