class OnlineShopAccount:
    def __init__(self,username:str,balance:int):
        self.username=username 
        self.balance=balance 
        self._items=[]#dont use
        self._items_price=[]#dont use
    
    def add_funds(self,amount:int):
        self.balance+=amount
    def buy_item(self,item_name:str, price:int):
        if self.balance>=price:
            self.balance-=price
            print(f"You have bought {item_name} for {price} euro.")
            self._items.append(item_name)
            self._items_price.append(price)
        else:
            print("You dont have enough funds.")
    def refund(self):
        print("You have bought:")
        for i in range(0,len(self._items)):
            print(f"{self._items[i]}: {self._items_price[i]} euro")
        item=str(input("What do you wanna refund?"))
        i=self._items.index(item)
        print(f"You have removed {self._items[i]} and have added {self._items_price[i]} to your balance.")
        self._items.remove(item)
        self._items_price.pop(i)
    def show_balance(self):
        print(f"You have {self.balance} euro.")


o= OnlineShopAccount("Kondev",67)
o.add_funds(41)
o.buy_item("Doner",5)
o.refund()
o.show_balance()