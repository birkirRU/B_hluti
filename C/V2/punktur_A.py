# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/22/2024>
# Verkefni: <Æfingarverkefni 2.1 A punktur>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    def sum(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return (x,y)

    
    def distance(self, point):
        x_1 = self.x
        x_2 = point.x
        y_1 = self.y
        y_2 = point.y
        return ( (x_2-x_1)**2 + (y_2-y_1)**2 )**0.5
    
    def move(self, a, b):
        self.x += a
        self.y += b
        return (self.x, self.y)


def main():
    my_point = Point(3,8)
    print(my_point)
    print(my_point.x)
    print(my_point.y)
    another_point = Point(9,7)
    dist = my_point.distance(another_point)
    print(dist)
    the_sum = my_point.sum(another_point)
    print(the_sum)
    my_point.move(11,6)
    print(my_point)
    another_point = Point()
    print(another_point)

main()