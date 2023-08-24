choice = 0 #ตัวแปรรับค่าเมนู

while choice != 5:             #<--วนลูปถ้า choice ไม่เท่ากับ 5 จะหลุด loop
    print("Choose a menu")  #print แสดงเมนูที่มีให้เลือกกรอก เลข ข้างหน้า
    print("1 = menu 1")     #print แสดงเมนูที่มีให้เลือกกรอก เลข ข้างหน้า
    print("2 = menu 2")     #print แสดงเมนูที่มีให้เลือกกรอก เลข ข้างหน้า
    print("3 = menu 3")     #print แสดงเมนูที่มีให้เลือกกรอก เลข ข้างหน้า
    print("4 = menu 4")     #print แสดงเมนูที่มีให้เลือกกรอก เลข ข้างหน้า
    print("5 = exit  ")     #print แสดงเมนูที่มีให้เลือกกรอก เลข ข้างหน้า

    choice = int(input("Input choice number : ")) #รับค่าจาก Keybord เก็บไว้ในตัวแปล Choice

    if choice == 1:           
        print ("Menu 1")       #<--ถ้ากรอกเลข 1
    elif choice == 2:
        print ("Menu 2")       #<--ถ้ากรอกเลข 2
    elif choice == 3:          
        print ("Menu 3")       #<--ถ้ากรอกเลข 3
    elif choice == 4:
        print ("Menu 4")       #<--ถ้ากรอกเลข 4
    elif choice == 5:
        print ("Exit")         #<--ถ้ากรอกเลข 5
        break                  #Break loop
    else:
        print("This menu is not available") #<--ถ้ากรอกเลข อื่นที่ไม่ใช่เลข 1-5 จะ print บรรทัดนี้
