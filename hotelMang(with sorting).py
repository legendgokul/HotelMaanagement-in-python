
import datetime
from datetime import timedelta

#Database stores all data of customer :
#[name,phone,address,checkin,checkout,roomType,price,restP]
Database=[]


def Home():
    print("\t\t WELCOME TO HOTEL LEMON TREE")
    print("\t\t\t 1. Booking")
    print("\t\t\t 2. Rooms Info")
    print("\t\t\t 3. Room Service(Menu Card)")
    print("\t\t\t 4. Payment")
    print("\t\t\t 5. Customer Record")
    print("\t\t\t 0. Exit")
    ch=int(input("Enter the choice: ")) 
    if ch==1: 
        Booking() 
    elif ch==2: 
        room_info()
    elif ch==3:
        restaurant()
    elif ch==4:
        payment()
    elif ch==5:
        record()
    else:
        exit()

def room_info(): 
    print("         ------ HOTEL ROOMS INFO ------") 
    print("") 
    print("GENRAL") 
    print("---------------------------------------------------------------") 
    print("ROOM FACLITIES: 1 Double Bed, Television, Telephone,") 
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
    print("an attached washroom with hot/cold water.\n") 
    print("DELUXE") 
    print("---------------------------------------------------------------") 
    print("ROOM FAC: 1 Double Bed, Television, Telephone,") 
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
    print("an attached washroom with hot/cold water + Window/Split AC.\n") 
    print("SUPER DELUXE") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1") 
    print("Side table, Balcony with an Accent table with 2 Chair and an") 
    print("attached washroom with hot/cold water.\n") 
    n=int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit()         

def payment():
    name=input("Enter name of Customer to do Payment: ")
    flag=0
    custNum=0
    for i in range(0,len(Database)):
        if Database[i][0] == name:
            flag=1
            custNum=i;
    if flag == 0:
        print("Customer not found")
        payment()
    else :
        print(" Payment") 
        print(" --------------------------------") 
        print("  MODE OF PAYMENT") 
        print("  1- Credit/Debit Card") 
        print("  2- Paytm/PhonePe") 
        print("  3- Using UPI") 
        print("  4- Cash") 
        x=int(input("-> "))
        print("\n            Pay For Lemon Tree") 
        print("  (y/n)") 
        ch=str(input("->"))
        if ch=='y' or ch=='Y': 
                print("\n\n --------------------------------") 
                print("           Hotel Lemon Tree") 
                print(" --------------------------------") 
                print("              Bill") 
                print(" --------------------------------") 
                print(" Name: ",Database[custNum][0],"\t\n Phone No.: ",Database[custNum][1],"\t\n Address: ",Database[custNum][2],"\t")  
                print("\n Room Type: ",Database[custNum][5],"\t\n Room Charges: ",Database[custNum][6],"\t") 
                print(" Restaurant Charges: ",Database[custNum][7]) 
                print(" --------------------------------") 
                print("\n Total Amount: ",Database[custNum][6] + Database[custNum][7],"\t") 
                print(" --------------------------------") 
                print("          Thank You") 
                print("          Visit Again :)") 
                print(" --------------------------------\n")

        # removing th customer detail
       
        Database.pop(custNum)
        n = int(input("0-BACK\n ->")) 
        if n==0: 
            Home() 
        else: 
            exit() 
        
def sortIt(data,ch) :

    if ch == 1:
        data.sort(key = lambda x: x[0])
        print("NAME \tPHONE NUMBER \t ADDRESS \t CHECK IN \t CHECK OUT \tRoomType \t Rent(Price)")
        for i in data:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6])
        
    elif ch == 2 :
        data.sort(key = lambda x: x[6])
        print("NAME \tPHONE NUMBER \t ADDRESS \t CHECK IN \t CHECK OUT \tRoomType \tRent(Price)")
        for i in data:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6])
      

    
       


def record():
    print("NAME \tPHONE NUMBER \t ADDRESS \t CHECK IN \t CHECK OUT \tRoomType \t Rent(Price)")
    for i in Database:
       print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6])

    print("Sort By :")
    print("1.Name")
    print("2.Total Expense :")
    choice = int(input("Enter sorting Preference:"))
    sortIt(Database,choice)


    n = int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit() 

# this fucntion takes 2 argument a data --> database and ch --> choice        

def DateCheck(Sday,Eday):
    #x holds current date when the program is running for more info check :
    #  https://www.w3schools.com/python/python_datetime.asp
    x = datetime.datetime.now()
    yesterday = x - timedelta(days = 1)
    if Sday<yesterday or Eday<yesterday :
        print("Sorry we cannot create record for past dates ")
        return False
    else :
        return True



def Booking():
    #n -- number of booking
    n=int(input("How many Booking: "))
    for i in range(n):
        print("Details for ",i+1," Booking:")
        name=input("Name:")
        phone=int(input("Phone Number :"))
        address=input("Address :")
        checkin=str(input("Check In  (Format : D/M/Y ) :"))
        checkout=str(input("Check Out (Format : D/M/Y ) :"))
        in_d=checkin
        out_d=checkout
        #price is normal room charge restP is restaurant purchase price
        price=0
        restP=0
        #converting string format of date to int
        in_d=in_d.split('/')
        for i in range(0, len(in_d)): 
            in_d[i] = int(in_d[i])

       
        #converting string format of date to int
        out_d=out_d.split('/')
        for i in range(0, len(out_d)): 
            out_d[i] = int(out_d[i])

        try :
            #Sday - starting date  Eday -ending date.
            Sday=datetime.datetime(in_d[2], in_d[1], in_d[0])
            Eday=datetime.datetime(out_d[2], out_d[1], out_d[0])
        except:
            print("Invalid date format")
            print("pls Try again ")
            Booking()

        # checking if date is valid
        if DateCheck(Sday,Eday) == False :
            print("Invalid Date")
            Booking()

        # checking if starting date is before end day
        if Eday < Sday:
           print("\n\tCheck-Out date must fall after Check-In\n")
           print("process terminating")
           booking()
          
        #checking roomType:
        pricePerDate=0
        print("----SELECT ROOM TYPE----") 
        print(" 1. Genral- Rs. 3500") 
        print(" 2. Deluxe - Rs. 4500 ")
        print(" 3. Super Deluxe - Rs. 5000")
        ch=int(input("->")) 
        if ch==1:            
            print("Room Type- Genral")   
            print("Price- 3500")
            pricePerDate = 3500 ;
            roomType=ch
        elif ch==2: 
            print("Room Type- Deluxe") 
            print("Price- 4500") 
            pricePerDate = 4500 ;
            roomType=ch
        elif ch==3: 
            print("Room Type- Super Deluxe") 
            print("Price- 5000")
            pricePerDate = 5000 ; 
            roomType=ch
        else: 
            print(" Wrong choice!!!")

        x = Eday - Sday
        #x will store a delta time format value oof the difference so we use .days to get just the day value
        days=x.days
        price = pricePerDate*days
        print("") 
        print("\t\t\t**ROOM BOOKED SUCCESSFULLY!**\n")     
        # data format as predefined
        customer=[name,phone,address,checkin,checkout,roomType,price,restP]
        
        #we are adding the data to the databse
        Database.append(customer)
    n=int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit() 
        
def room_info(): 
    print("         ------ HOTEL ROOMS INFO ------") 
    print("") 
    print("GENRAL") 
    print("---------------------------------------------------------------") 
    print("ROOM FACLITIES: 1 Double Bed, Television, Telephone,") 
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
    print("an attached washroom with hot/cold water.\n") 
    print("DELUXE") 
    print("---------------------------------------------------------------") 
    print("ROOM FAC: 1 Double Bed, Television, Telephone,") 
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
    print("an attached washroom with hot/cold water + Window/Split AC.\n") 
    print("SUPER DELUXE") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1") 
    print("Side table, Balcony with an Accent table with 2 Chair and an") 
    print("attached washroom with hot/cold water.\n") 
    n=int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit() 
            
def restaurant():
            custNum=0
            print("-------------------------------------------------------------------------") 
            print("                           Hotel lemon Tree") 
            print("-------------------------------------------------------------------------") 
            print("                            Menu Card") 
            print("-------------------------------------------------------------------------") 
            print("\n BEVARAGES                              26 Dal Fry................ 140.00") 
            print("----------------------------------      27 Dal Makhani............ 150.00") 
            print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00") 
            print(" 2  Masala Tea.............. 25.00") 
            print(" 3  Coffee.................. 25.00      ROTI") 
            print(" 4  Cold Drink.............. 25.00     ----------------------------------") 
            print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00") 
            print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00") 
            print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00") 
            print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00") 
            print(" 9  Cheese Toast Sandwich... 70.00") 
            print(" 10 Grilled Sandwich........ 70.00      RICE")  
            print("                                       ----------------------------------") 
            print(" SOUPS                                  33 Plain Rice.............. 90.00") 
            print("----------------------------------      34 Jeera Rice.............. 90.00") 
            print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00") 
            print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00") 
            print(" 13 Veg. Noodle Soup....... 110.00") 
            print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN") 
            print(" 15 Veg. Munchow........... 110.00     ----------------------------------") 
            print("                                        37 Plain Dosa............. 100.00") 
            print(" MAIN COURSE                            38 Onion Dosa............. 110.00") 
            print("----------------------------------      39 Masala Dosa............ 130.00") 
            print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00") 
            print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00") 
            print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00") 
            print(" 19 Palak Paneer........... 120.00") 
            print(" 20 Chilli Paneer.......... 140.00      ICE CREAM") 
            print(" 21 Matar Mushroom......... 140.00     ----------------------------------") 
            print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00") 
            print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00") 
            print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00") 
            print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00") 
            print("Press 0 -to end OR Press 1 to Enter customer name and buy food")
            n=int(input("->"))
            if n == 1 :
                name=input("Enter  customer name:")
                # we are setting flag to 0 (no customer) and we will change it to 1 when we find our customer in database:
                flag=0
                try :
                    for i in range(0,len(Database)):
                        if Database[i][0] == name:
                            flag=1
                            custNum=i
                except:
                    print("customer not found")
                    restaurant()
                    
            else :
                Home()
            ch=1
            r=0
            if flag==1:
                print("Enter food numbers to order:")
                while(ch!=0): 
                    ch=int(input(" -> ")) 
                    if ch==1 or ch==31 or ch==32: 
                        rs=20
                        r=r+rs 
                    elif ch<=4 and ch>=2: 
                        rs=25
                        r=r+rs 
                    elif ch<=6 and ch>=5: 
                        rs=30
                        r=r+rs 
                    elif ch<=8 and ch>=7: 
                        rs=50
                        r=r+rs 
                    elif ch<=10 and ch>=9: 
                        rs=70
                        r=r+rs 
                    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38: 
                        rs=110
                        r=r+rs 
                    elif ch<=19 and ch>=18: 
                        rs=120
                        r=r+rs 
                    elif (ch<=26 and ch>=20) or ch==42: 
                        rs=140
                        r=r+rs 
                    elif ch<=28 and ch>=27: 
                        rs=150
                        r=r+rs 
                    elif ch<=30 and ch>=29: 
                        rs=15
                        r=r+rs 
                    elif ch==33 or ch==34: 
                        rs=90
                        r=r+rs 
                    elif ch==37: 
                        rs=100
                        r=r+rs 
                    elif ch<=41 and ch>=39: 
                        rs=130
                        r=r+rs 
                    elif ch<=46 and ch>=43: 
                        rs=60
                        r=r+rs 
                    elif ch==0: 
                        pass
                    else: 
                        print("Wrong Choice..!!") 
                print("Total Bill: ",r)
                #we are updating the price
                Database[custNum][7]=Database[custNum][7] + r

                print("Price Updated, Thanks for Buying ")

            else:
                print("customer not found")  
                n=int(input("0-BACK\n ->")) 
                if n==0: 
                    Home()    
    

#starting point
Home()
