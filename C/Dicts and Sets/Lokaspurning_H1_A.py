# Höfundur: <Birkir Snær Axelsson>
# Dagsetning: <10/18/2024>
# Verkefni: <Lokaspurning H1 A Matseðill>
# Athugasemdir: <ef þú þáðir eða veittir aðstoð þá á það að vera tekið fram hér, einnig aðrar
# athugasemdir sem þú vilt koma á framfæri við þann sem fer yfir verkefnið>
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða annars aðila): <Já>


menu = {
    "Hamborgari": 1500,
    "Pasta": 1390,
    "Nautasteik": 3800,
    "Lax": 1900,
    "Salat": 1200,
    "Pizza": 2800
}


def add_item(food, price):
    menu[food] = price
    print(f"{food} hefur verið settur á matseðlin.")

def remove_item(item):
    try:
        menu.pop(item)
        print(f"{item} hefur verið fjarlægður af á matseðlinum.")
    except KeyError:
        print("Réttur fannst ekki á matseðli")
    
def update_price(food, new_price): # Þarf kannski að laga, furðuleg leið hvernig farið er að þessu.
    try:
        menu.pop(food)
        menu[food] = new_price
        print(f"{food} hefur verið upfærður á matseðlinum")

    except KeyError:
        print("Réttur fannst ekki á matseðli")

def get_price(food):
    try:
        return f"Réttur {food}. Verð: {menu[food]}"
    except KeyError:
        return "Réttur finnst ekki á matseðli"
    
def take_order(menu):
    o_nr = 1
    s_order = input(f"({o_nr}) Sláðu inn rétt til þess að panta, \n 'q' til þess að hætta: ")
    c_order = {"Pöntun": []}


    while s_order != "q":
        o_nr+=1
        c_order["Pöntun"].append(s_order)
        s_order = input(f"({o_nr}) Sláðu inn rétt til þess að panta, \n 'q' til þess að hætta: ")


    price_list = [menu[food] for food in [order for order in c_order["Pöntun"]]]
    o_sum = sum(price_list)

    print(c_order)
    print(f"Heildarkostnaður pöntunar: {o_sum}")



def display_menu(menu):
    print("-------------------------------------------")
    print("Matseðill:")
    for meal in menu: # kannski menu.keys()
        print(f"Réttur: {meal}. Verð: {menu[meal]}")

def display_options():
    print("-------------------------------------------")
    print("1. > Bæta við rétt á matseðil")
    print("2. > Fjarlægja af matseðli")
    print("3. > Upfæra verð réttar")
    print("4. > Fá verð á rétti")
    print("5. > Taka pöntun")
    print("6. > Sýna matseðil")
    print("9. > Hætta")

def main():
    display_options()
    option = int(input("Veldu valmöguleika: "))
    while option != 9:
        if option == 1:
            food, price = list(map(str, input("Sláðu inn --> mat, verð: ").split(", ")))
            add_item(food, int(price))
        elif option == 2:
            food = input("Sláðu inn til þess að fjarlægja--> mat : ")
            remove_item(food)
        elif option == 3:
            food, price = list(map(str, input("Sláðu inn --> mat, verð: ").split(", ")))
            update_price(food, int(price))
        elif option == 4:
            food = input("Sláðu inn til þess að fjarlægja--> mat : ")
            price = get_price(food)
            print(price)
        elif option == 5:
            take_order(menu)
        elif option == 6:
            display_menu(menu)
        display_options()
        option = int(input("Veldu valmöguleika: "))
    

main()