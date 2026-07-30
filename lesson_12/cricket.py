class Cricket:
    def __init__(self,player,score):
        self.__player=player
        self.__score=score
    def info(self):
        print(f"the name is {self.__player} and score is {self.__score}")

    def play(self):
        print(f'{self.player} hit a six!!')

    def get_score(self):
        return self.__score
    def set_score(self,score):
        if score>=0:
            self.__score=score
            print(f'score is now {self.__score}')
        else:
            print('invalid score')
    def get_name(self):
        return self.__player


    

class Football:
    def __init__(self,player,score):
        self.__player=player
        self.__score=score
    def info(self):
        print(f"the name is {self.__player} and score is {self.__score}")

    def play(self):
        print(f'{self.player} SCORES A GOAL!!')

    def get_score(self):
        return self.__score
    def set_score(self,score):
        if score>=0:
            self.__score=score
            print(f'score is now {self.__score}')
        else:
            print('invalid score')
    def get_name(self):
        return self.__player
        

a=Football('cristiano',1000)
b=Cricket('rohit',10000)
for i in (a,b):
    i.info()
    print(i.get_score())
    i.set_score(500)
    
