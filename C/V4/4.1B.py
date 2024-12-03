
# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/28/2024>
# Verkefni: <Strengjamengi>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>

class StringSet:
    def __init__(self, string=""):
        self.string = string
        self.string_set = []
        
        for word in string.split(" "):
            if not self.find_(word):
                self.string_set.append(word)
    
    def __str__(self):
        return f"{self.string}"

    def add(self, word):
        if not self.find(word):
            self.string_set.append(word)
    
    def __add__(string1, string2):

        set1 = string1.string_set 
        set2 = string2.string_set
        union_string = ""
        for word in set1:
            union_string += word + " "

        for word in set2:
            if not string1.find_(word):
                if set2.index(word) != len(set2)-1:
                    union_string += word + " "
                else:
                    union_string += word
        
        # Sniðugri lausn

        # union_set = StringSet("")
        # for word in string1:
        #     union_set.string_set.append(word)
        # for word in string2:
        #     union_set.string_set.append(word)
        # return union_set

        return StringSet(union_string)

    def find_(self, word):
        return word in self.string_set
    
    def at(self, index):
        return self.string_set[index]

    def size(self):
        return len(self.string_set)
    

def main():
    str1 = 'chocolate ice cream and chocolate candy ice bars are my favorite'
    set1 = StringSet(str1)
    str2 = 'I like to eat broccoli and fish and ice cream and brussel fish sprouts'
    set2 = StringSet(str2)
    print("Set1:", set1)
    print("Set2:", set2)
    print("Set1 size:", set1.size())
    print("Set2 size:", set2.size())
    the_union = set1 + set2
    print("Union:", the_union)
    print("Union size:", the_union.size())
    query = StringSet('chocolate cream fish good rubbish')
    print("Query:", query)
    count = 0
    for i in range(query.size()):
        if the_union.find_(query.at(i)):
            count += 1
    print("Query size:", query.size())
    print("Found in union:", count)


main()