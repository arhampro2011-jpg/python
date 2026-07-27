from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name,habitat):
        self.name=name
        self.habitat=habitat

    def display(self):
        print(f'name is {self.name} habitat is {self.habitat}')

    def intro(self):
        print(f'hi i am {self.name}')

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed=breed
    def intro(self):
        print(f"name is {self.name} and breed is {self.breed}")

    def speak(self):
        print('woof')


class Parrot(Animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed=breed
    def intro(self):
        print(f"name is {self.name} and breed is {self.breed}")

    def speak(self):
        print('i repeat what you say')

class Lion(Animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed=breed
    def intro(self):
        print(f"name is {self.name} and breed is {self.breed}")

    def speak(self):
        print('roar')
    
d=Dog('tommy','home','golden retriever')


p=Parrot('polly','jungle','macau')


l=Lion('simbba','jungle','male')
for i in [d,p,l]:
    i.display()
    i.intro()
    i.speak()