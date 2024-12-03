# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/22/2024>
# Verkefni: <Bank account>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>


class BankAccount:
    def __init__(self, bank_number, status=0) -> None:
        self.b_nr = bank_number
        self.status = status

    def __str__(self):
        return f"Númer bankareiknings: {self.b_nr}\nStaða {self.status} kr"

    def deposit(self, money):
        if money < 0:
            print("Upphæð verður að vera jákvæð tala.")
        else:
            self.status += money


    
    def withdraw(self, money):
        if money > self.status:
            print("Ekki er næg innistæða á reikningnum fyrir þessa úttekt.")
        else:
            self.status -= money
    
    def get_balance(self):
        return self.status


def main():
    account = BankAccount("12345")
    print(account)
    account.deposit(1000)
    print(account)
    account.withdraw(5000)
    account.withdraw(800)
    print(account)
    account.deposit(-700)
    account.deposit(200)
    print(account)

main()