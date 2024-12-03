
# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/28/2024>
# Verkefni: <Shopping Cart>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>


class ShoppingCart:
    def __init__(self) -> None:
        self.total = 0
        self.cart_amount = {}
        self.cart_price = {}

    def __str__(self):
        final_string = ""
        for product in self.cart_price:
            final_string += product
            final_string += ': ' 
            final_string += str(self.cart_amount[product])
            final_string += ' x '
            final_string += str(self.cart_price[product])
            final_string += 'kr'
            final_string +=  '\n'
        
        return f'Innihald Körfu \n{final_string}Heildarverð: {self.total} kr'
        
    def add_item(self, name, price, amount):
        if name in self.cart_price:
            self.cart_amount[name] += amount
        else:   
            self.cart_amount[name] = amount
            self.cart_price[name] = price
        
        self.cart_price[name] = price
        self.total += price*amount
    
    def remove_item(self, name, amount=1):

        if amount == 1:
            price = self.cart_price[name]
            self.cart_amount[name] -= 1
            self.total -= price
        else:
            if self.cart_amount - amount <= 0:
                self.cart_price.pop(name)
                self.cart_amount.pop(name)
            else:
                price = self.cart_price[name]
                self.cart_amount[name] -= amount
                self.total -= price * amount


    def update_quantity(self, name, quantity):
        old_quantity = self.cart_amount[name]
        self.cart_amount[name] = quantity
        self.total += self.cart_price[name] * (quantity - old_quantity)

    def clear_cart(self):
        self.total = 0
        self.cart_amount = {}
        self.cart_price = {}

    def calculate_total_cost(self):
        total_cost = 0
        for price, amount in zip(self.cart_price.values(), self.cart_amount.values()):
            total_cost += price * amount
        return total_cost

def main():
    cart = ShoppingCart()
    cart.add_item("Dúnúlpa", 8990, 2)
    cart.add_item("Gönguskór", 14990, 1)
    cart.add_item("Göngustafir", 6990, 1)
    print(cart)
    cart.update_quantity("Gönguskór", 2)
    print(cart)
    cart.remove_item("Dúnúlpa")
    print(cart)
    cart.clear_cart()
    print(cart)

main()