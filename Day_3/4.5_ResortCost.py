import questionary
class1 = dict(name = "Standard", price = 1260000 )
class2 = dict(name = "Superior Garden View", price = 1550000 )
class3 = dict(name = "Superior Ocean View", price = 1830000)
class4 = dict(name = "Garden View Bungalow", price = 1830000)
class5 = dict(name = "Pool View Bungalow", price = 2120000)
class6 = dict(name = "Family Room ", price = 2120000)
class7 = dict(name = "Beach Front Bungalow ", price = 2540000)
class8 = dict(name = "VIP sea view ", price = 4800000)

roomtype = class1

busquestion = questionary.select(
        "What room type do you want?",
        choices=[
            class1["name"],
            class2["name"],
            class3["name"],
            class4["name"],
            class5["name"],
            class6["name"],
            class7["name"],
            class8["name"],
    ])
roomtype = (busquestion.ask())

print('\x1b[6;30;42m' + 'Customer Selected: ', roomtype + '\x1b[0m')

days = int(input("How many night will you be staying? "))

def calculate(typeprice):
    if days < 0:
        print("Invalid number")
    elif days == 1:
        print('Type Chosed:',roomtype)
        print('Days:',days)
        print(f"Total: {typeprice:,} VND")
    elif days == 3 or 2:
        discount = (typeprice*days)*.25
        totalprice = typeprice*days - discount
        print('Type Chosed:',roomtype)
        print('Days:',days)
        print(f"Discount: {discount:,} VND")
        print(f"Total: {totalprice:,} VND")
        
    elif days >= 4:
        discount = (typeprice*days)*.30
        totalprice = typeprice*days - discount
        print('Type Chosed:',roomtype)
        print('Days:',days)
        print(f"Discount: {discount:,} VND")
        print(f"Total: {totalprice:,} VND")


def typesort():
    if roomtype == class1["name"]:
        calculate(class1["price"])
    elif roomtype == class2["name"]:
        calculate(class2["price"])
    elif roomtype == class3["name"]:
        calculate(class3["price"])
    elif roomtype == class4["name"]:
        calculate(class4["price"])
    elif roomtype == class5["name"]:
        calculate(class5["price"])
    elif roomtype == class6["name"]:
        calculate(class6["price"])
    elif roomtype == class7["name"]:
        calculate(class7["price"])
    elif roomtype == class8["name"]:
        calculate(class8["price"])

typesort()





