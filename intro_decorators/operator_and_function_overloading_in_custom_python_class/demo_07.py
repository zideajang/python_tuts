class Favority:
    def __init__(self, favority, user):
        self.favority = list(favority)
        self.user = user
    
    def __len__(self):
        return len(self.favority)

    def __add__(self,tut):
        new_favority = self.favority.copy()
        new_favority.append(tut)
        return Favority(new_favority,self.user)

    def __getitem__(self,key):
        return self.favority[key]

    def __iadd__(self,tut):
        self.favority.append(tut)
        return self

    

favority = Favority(['machine leanring','deep learning','reinforcement leanring'],'mike')
favority += 'pytroch tut'
favority += 'tensorflow tut'
# ['machine leanring', 'deep learning', 'reinforcement leanring', 'pytroch tut', 'tensorflow tut']
print(favority.favority)
