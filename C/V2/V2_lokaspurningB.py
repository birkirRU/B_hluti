# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/22/2024>
# Verkefni: <Lokaspurning H2 B Klasar Brot>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>


class Fraction:
    def __init__(self, nefnari=1, teljari=1) -> None:
        self.n = nefnari
        self.d = teljari
    
    def __add__(self, frac):
        same_d = self.d * frac.d
        numerator = self.d* self.n + frac.n * frac.d
        return Fraction(numerator, same_d)


    def __sub__(self, frac):
        same_d = self.d * frac.d
        numerator = self.d* self.n - frac.n * frac.d
        return Fraction(numerator, same_d)

    def __float__(self):
        return self.n / self.d

    def __str__(self):
        return f"{self.n}/{self.d}"

    def inverse(self):
        return Fraction(self.d, self.n)
    
def main():
    a = Fraction(1,4)
    b = Fraction(3,4)
    c = a + b
    print("a:", a)
    print("b:", b)
    print("a + b =", c)
    print(float(c))
    d = b - a
    print("b - a =", d)
    print(a.inverse())
    print(b.inverse())

main()