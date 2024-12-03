# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/26/2024>
# Verkefni: <Erfðir Hringur> 
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>
import math

class Circle:
    def __init__(self, rad) -> None:
        self.rad = rad

    def __str__(self):
        return f"Circle with radius: {self.rad}"

    def area(self):
        return (self.rad**2) * math.pi

    def perimeter(self):
        return 2*self.rad*math.pi

    
class Cylinder(Circle):
    def __init__(self, rad, height) -> None:
        Circle.__init__(self, rad) # super().__init__(rad) virkar líka
        self.height = height

    def __str__(self):
        return f"Cylinder with radius: {self.rad} and height {self.height}"

    def volume(self):
        return super().area() * self.height 
    
    def surface(self):
        return super().perimeter() * self.height + 2*super().area()
    
