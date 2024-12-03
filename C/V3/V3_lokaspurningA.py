# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/22/2024>
# Verkefni: <Lokaspurning H3 A salary Starfsmaður>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>

class Employee:
    def __init__(self, id, name) -> None:
        self.name = name
        self.id = id

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary) -> None:
        super().__init__(id, name)
        self.weekly_salery = weekly_salary

    def calculate_salery(self):
        return self.weekly_salery

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate) -> None:
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_salery(self):
        return self.hours_worked*self.hour_rate   

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commision) -> None:
        super().__init__(id, name, weekly_salary)
        self.commision = commision
        self.weekly_salery = weekly_salary

    def calculate_salery(self):
        return self.weekly_salery + self.commision
    

def main():
    salary_employee = SalaryEmployee(1, 'Guðmundur Jónsson', 150000)
    hourly_employee = HourlyEmployee(2, 'Sigríður Arnarsdóttir', 40, 3200)
    commission_employee = CommissionEmployee(3, 'Anna Einarsdóttir', 150000, 40000)
    all_employees = [salary_employee, hourly_employee, commission_employee]
    calculate_payroll(all_employees)

def calculate_payroll(employee_list):
    print("Launaupplýsingar")
    print("================")

    for employee in employee_list:
        print(f"{employee.name}: {employee.calculate_salery()}")

main()