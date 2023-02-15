from admin import *
from user import *
import json
import sys
if __name__ == '__main__':
    food_list = [("Tandoori Chicken", "4 pieces", 240), ("Vegan Burger", "1 Piece", 320), ("Truffle Cake", "500gm", 900)]
    admin=Admin()
    user=User()


    while True:
        print("*"*30+" WELCOME TO FOOD ORDERING APP "+"*"*30)
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            if username == "Akhil" and password == "Akhil123":
                print("*"*30+" LOGIN SUCCESSFULLY! "+30*"*")
                
                while True:
                    print("1. Add Food")
                    print("2. Edit Food")
                    print("3. Remove Food")
                    print("4. View Food")
                    print("5. Logout")
                    choice = int(input("Enter your choice: "))
                    
                    if choice == 1:
                        admin.add_food()
                        print("*"*90)
                        
                    if choice == 2:
                        admin.edit_food()
                        print("*"*90)
                        
                    if choice == 3:
                        admin.remove_food()
                        print("*"*90)
                        
                    if choice == 4:
                        print(admin.view_food())
                        print("*"*90)
                        
                    if choice==5:
                        print("*"*30+" LOGOUT SUCCESSFULLY! "+30*"*")
                        sys.exit()
                        
        if choice==2:
            print("Register a account")
            user.register()
            print("Registered successfully")
            print("Login into the account")
            user.login()
            
            while True:
                print("1. Place new order")
                print("2. Order history")
                print("3. Update profile")
                print("4. Exit")
                option = int(input("Enter option number: "))
                
                if option == 1:
                    user.place_new_order(food_list)
                    print("*"*100)
                    
                elif option == 2:
                    user.order_history()
                    print("*"*100)
                    
                elif option == 3:
                    user.update_profile()
                    print("*"*100)
                    
                elif option == 4:
                    print("*"*30+" THANK YOU VISIT AGAIN! "+30*"*")
                    sys.exit()
                    
                else:
                    print("Invalid option,please enter valid option")

        if choice==3:
                print("*"*30+" THANK YOU VISIT AGAIN! "+30*"*")
                sys.exit()
                