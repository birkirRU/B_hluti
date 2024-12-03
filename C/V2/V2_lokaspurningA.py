# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/22/2024>
# Verkefni: <V2_lokaspurningA.py>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>

class OrderedPair:
    def __init__(self, x=0, y=0) -> None:
        self.ordered = sorted([x, y])
        self.x = self.ordered[0]
        self.y = self.ordered[1]


    def __add__(self, pair):
        return OrderedPair(self.x + pair.x, self.y + pair.y)
    
    def __sub__(self, pair):
        return OrderedPair(self.x - pair.x , self.y - pair.y)
    
    def __eq__(self, pair):
        return (self.x == pair.x) and (self.y == pair.y)
       
   
    def __ge__(self, pair):
        self_sum = self.x + self.y
        pair_sum = pair.x + pair.y
        return self_sum >= pair_sum
        
    
    def __str__(self):
        return "({} {})".format(self.x, self.y)


    def set_element(self, index, value):
        if index == 0:
            if self.x >= value:
                self.x = value
                self.y = self.ordered[::-1][1]
                self.ordered[0] = value
                self.ordered[1] = self.y
            elif self.x < value:
                self.y = value
                self.ordered[1] = value

        elif index == 1:
            if self.y >= value:
                self.x = value
                self.ordered[0] = value
            elif self.y < value:
                self.y = value
                self.ordered[1] = value



def main():
    print('----- testing init ----------')
    a = OrderedPair()
    print('a =', a)
    b = OrderedPair(2,4)
    print('b =', b)
    c = OrderedPair(5,3)
    print('c =', c)
    print('------- testing set element ————')
    # set_element fallið tekur inn index og gildi
    # þ.e. set_element(0,8) segir að við eigum að breyta gildinu á fyrra stakinu í 8
    a.set_element(0,8)
    print('a(0) = 8')
    print('a =', a)
    a.set_element(0,4)
    print('a(0) = 4')
    print('a =', a)
    a.set_element(1,3)
    print('a(1) = 3')
    print('a =', a)
    print('-------- testing plus and minus ---------')
    d = a + b
    print('a + b =',d)
    e = b - a
    print('b - a =',e)
    print('-------- testing equal and greater-than-or-equal ————')
    # Samanburður virkar þannig að við leggjum saman tölurnar og berum saman
    # summu þeirra
    if e >= d:
        print(e, '>=', d)
    else:
        print(e, '<', d)
    # Tvö OrdererdPair er eins ef þau innihalda sömu tölur.
    if b == c:
        print(b,'and', c, 'are equal')
    else:
        print(b,'and', c, 'are not equal')
    if b == OrderedPair(4,2):
        print(b,'is (2,4)')


main()