class Wallet:
    def __init__(self,balance,currency):
        self.balance=balance
        self.currency=currency
    
    def add_money(self,amount):
        self.balance+=amount
        print(f"You added {amount}{self.currency}.")
    
    def spend_money(self,amount):
        if amount>self.balance:
            print("Insufficient availability.")
            return
        else:
            self.balance-=amount
            print(f"You spent {amount}{self.currency}.")

    def show_balance(self):
        print(f"You have {self.balance}{self.currency}.")
        return
    
    def convert_curr(self):
        if self.currency=="BGN":
            print("Converting BGN to EUR...")
            self.currency="EUR"
            self.balance*=0.51
            print(f"Balancy now is {self.balance}{self.currency}.")
            return
        elif self.currency=="EUR":
            print("Converting EUR to BGN...")
            self.currency="BGN"
            self.balance/=0.5
            print(f"Balancy now is {self.balance}{self.currency}.")
            return



a=Wallet(100,"BGN")
a.add_money(100)
a.spend_money(50)
a.show_balance()
a.convert_curr()