class Student:
    name=input('what is your name')
    grade=input('what is your grade')
    def intro(self):
        print('i am a student')
    def details(self):
        print(f'my name is {self.name}, my grade is {self.grade}')

arham=Student()
arham.intro()
arham.details()