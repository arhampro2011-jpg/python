class Robo:
    def __init__(self,name,age,price):
        self.name=name
        self.age=age
        self.price=price
    
    def intro(self):
        print(f'my name is {self.name}. i am {self.age} yrs old and i cost {self.price} dollars')

tom=Robo('tom','2','200')

jerry=Robo('jerry','3','500')

tom.intro()
jerry.intro()