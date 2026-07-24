class Animal:
    
    species='bird'
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def display(self):
        print(f'the name is {self.n} and age is {self.a}')
    

parrot=Animal('joey',5)
parrot.display()
print(parrot.species)
name_temp=input('what is the name of your doggy')
age_temp=input('what is the age of your doggy')
dog=Animal(name_temp,age_temp)
dog.display()