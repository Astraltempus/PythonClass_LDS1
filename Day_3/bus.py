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
            # # code của bạn
            # distanceprice = km * 11000 # ở đây là đồng/0.8km

            # đổi ở đây
            distanceprice = km * 11000 * 10/8 # đây là đã đổi qua đồng/km
        elif km <= 31: # là trường hợp 2 bao gồm  0.8 km đầu là 0.8km với tiền là 11000 * 10/8 và (km - 0.8)km sau với tiền là 15300 đồng/km
            distanceprice = (0.8 * 11000 * 10/8) + (km-0.8) * 15300
        else: # trường hợp cuối 0.8 km với 11000 * 10/8 và (31-0.8) km sau và (km-31) km cuối
            distanceprice = 0.8 * 11000 * 10/8 + (31-0.8) * 15300 + (km-31) * 12100
        total = distanceprice + idleprice
        print("IdlePrice: ", idleprice)
        print("DistancePrice: ", distanceprice)
        print("Total: ", total)

        # # ra dạng 100,000,000
        # print(f"IdlePrice:  {idleprice:,}")
        # print(f"DistancePrice: {distanceprice:,}")
        # print(f"Total: {total:,}")
    if btype == '7 seats':
        # tương tự
        idleprice = (wtime - 5) * 750
        if km <= 0.8:
            distanceprice = km * 12000 * 10/8
        elif km <= 31:
            distanceprice = (0.8 * 12000 * 10/8) + (km-0.8) * 16100
        else:
            distanceprice = (0.8 * 12000 * 10/8) + (31-0.8) * 16100 + (km-31) * 13800
        total = distanceprice + idleprice
        print("IdlePrice: ", idleprice)
        print("DistancePrice: ", distanceprice)
        print("Total: ", total)

        # # ra dạng 100,000,000
        # print(f"IdlePrice:  {idleprice:,}")
        # print(f"DistancePrice: {distanceprice:,}")
        # print(f"Total: {total:,}")

calculate()