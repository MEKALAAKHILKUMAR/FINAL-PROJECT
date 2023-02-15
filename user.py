import json
import sys

class User:
    
    def register(self):
        self.name = input("enter full name: ")
        self.phone = int(input("enter phone number: "))
        self.email = input("enter email: ")
        self.address =input("enter address: ")
        self.password = input("enter password: ")
        self.orders = []
        
    def login(self):
        email=input("enter email: ")
        password=input("enter password: ")
        if self.email==email and self.password==password:
            print("*"*30+"LOGIN SUCCESSFULLY!"+30*"*")
        else:
            print("invalid log in attempt")
            print("try to login again")
            #user.login()
            
            
    def update_profile(self):
        self.name = input("enter name: ")
        self.phone = int(input("enter phone nmber: "))
        self.email = input("enter email: ")
        self.address =input("enter adddress: ")
        self.password = input("enter password: ")
        print("Profile updated successfully")
        
        
    def place_new_order(self, food_list):
        for i, food in enumerate(food_list):
            print(i+1,food_list[i])
            
        
        selected_food = map(int,input("Enter the numbers of the food items separated by comma: ").split(","))
        selected_food = [int(x) for x in selected_food]

   
        print("Selected food items:")
        for i in selected_food:
            print(food_list[i-1])
    
        
        order_confirm = input("Do you want to place the order? (yes/no)")
        if order_confirm.lower() == "yes" or "YES":
            self.orders.append([food_list[i - 1] for i in selected_food])
            print("Order placed successfully!")
        with open("order.json","w") as f:
            json.dump(self.orders,f)
        return ""
            
            

    def order_history(self):
        print("Order history:")
        for order in self.orders:
            print(order)
        with open("order.json","w") as f:
            json.dump(self.orders,f)
        return ""

food_list = [("Tandoori Chicken", "4 pieces", 240), ("Vegan Burger", "1 Piece", 320), ("Truffle Cake", "500gm", 900)]
       
    
