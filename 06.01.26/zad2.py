class Player:
    def __init__(self,name:str):
        self.name=name
        self._energy=100#dont use
        self._health=100#dont use
    
    def attack(self):
        if self._energy==0:
            print("You dont have enough enery to attack.")
        self._energy-=5
        print(f"You attacked and you have {self._energy} energy.")
    def take_damage(self,amount):
        if self._health>=amount:
            self._health-=amount
            if(self._health==0):
                print("You died.")
                return
            print(f"You took {amount} dmg and have {self._health} now.")
        else:
            self._health=0
            print("You died.")
    def heal(self,amount):
        if amount+self._health>100:
            self._health=100
        else:
            self._health+=amount
        print(f"You healed to {self._health} hp.")
    def status(self):
        print(f"You are on {self._health} hp and have {self._energy} energy.")

o=Player("1")
o.attack()
o.take_damage(20)
o.heal(15)
o.status()