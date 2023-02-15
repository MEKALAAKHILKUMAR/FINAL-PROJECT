import json
import sys

class Admin:
    
    def __init__(self):
        self.food_items={}
        self.food_id=len(self.food_items)+1
        
    def add_food(self):
        self.name=input("enter food name: ")
        self.quantity=int(input("enter quantity: "))
        self.price=int(input("enter price: "))
        self.discount=int(input("enter discount: "))
        self.stock=int(input("enter stock: "))
        self.item={"food name":self.name,"quantity":self.quantity,"price":self.price,"discount":self.discount,"stock":self.stock}
        self.food_id=len(self.food_items)+1
        self.food_items[self.food_id]=self.item
       
        with open("fooditems.json","w") as f:
            json.dump(self.food_items,f)
        return self.food_items
    
    
    def edit_food(self):
        food_id=int(input("enter food id: "))
        self.food_items[food_id]["food name"]=input("enter food name: ")
        self.food_items[food_id]["quantity"]=int(input("enter quantity: "))
        self.food_items[food_id]["price"]=int(input("enter price: "))
        self.food_items[food_id]["discount"]=int(input("enter discount: "))
        self.food_items[food_id]["stock"]=int(input("enter stock: "))
        
        with open("fooditems.json","w") as f:
            json.dump(self.food_items,f)
        return self.food_items
    
    
    def view_food(self):
        return self.food_items
    
    
    def remove_food(self):
        self.food_id=int(input("enter food id to remove: "))
        del self.food_items[self.food_id]
        
        with open("fooditems.json","w") as f:
            json.dump(self.food_items,f)
        return self.food_items
    
    
