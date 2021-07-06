import questionary
btype = ''



busquestion = questionary.select(
        "How many seats? 4 or 7?",
        choices=[
            '4 seats',
            '7 seats',
    ])
btype = (busquestion.ask())

#def bustype():
#   print('4) 4 Seat')
#   print('7) 7 Seat')]
#    inputtype = int(input("Type 4 or 7:  "))
#    btype = inputtype


km = int(input("How many Kilometer? "))
wtime = int(input("How long was the waiting time?  "))

def calculate():
    if btype == '4 seats':
        idleprice = (wtime - 5) * 750
        if km <= 0.8:
            distanceprice = km * 11000
        if km <= 30:
            distanceprice = km * 15300
        if km >= 31:
            distanceprice = km * 12100
        total = distanceprice + idleprice
        print("IdlePrice: ", idleprice)
        print("DistancePrice: ", distanceprice)
        print("Total: ", total)
    if btype == '7 seats':
        idleprice = (wtime - 5) * 750
        if km <= 0.8:
            distanceprice = km * 12000
        if km <= 30:
            distanceprice = km * 16100
        if km >= 31:
            distanceprice = km * 13800
        total = distanceprice + idleprice
        print("IdlePrice: ", idleprice)
        print("DistancePrice: ", distanceprice)
        print("Total: ", total)

calculate()

