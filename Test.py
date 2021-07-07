#IGNORE!!! I test random stuff here lmao
# Assist Hoang Vo

loai_1 = 1260000 #Standard
loai_2 =  1550000 #Sup_garden_view
loai_3 =  1830000 #Sup_ocean_view
loai_4 =  1830000 #Garden_view_bungalow
loai_5 =  2120000 #Pool_View_Bungalow
loai_6 =  2120000 #Family_room
loai_7 = 2540000 # Beach_Front_bungalow
loai_8 =  4800000 #VIP_sea_view

loai_phong = int(input("Nhập loại phòng (Từ 1 đến 8): "))

if loai_phong == 1: 
    loai_phong = loai_1
elif loai_phong == 2:  
    loai_phong = loai_2
elif loai_phong == 3:  
    loai_phong = loai_3
elif loai_phong == 4:  
    loai_phong = loai_4
elif loai_phong == 5:  
    loai_phong = loai_5
elif loai_phong == 6:  
    loai_phong = loai_6
elif loai_phong == 7:  
    loai_phong = loai_7
elif loai_phong == 8:  
    loai_phong = loai_8

so_dem = int(input("Nhập số đêm:"))

thanh_tien = loai_phong * so_dem

#tính số đêm
if so_dem == 1:
    print(f"Total: {thanh_tien:,} VND")

elif so_dem <= 3:
    giam_2_dem = thanh_tien*.25
    print(f"Total: {giam_2_dem:,} VND")
    total = thanh_tien - giam_2_dem
    print(f"Total: {total:,} VND")

elif so_dem >= 4: 
    giam_4_dem = thanh_tien*.30 
    print(f"Total: {giam_4_dem:,} VND")
    total = thanh_tien - giam_4_dem
    print(f"Total: {total:,} VND")

