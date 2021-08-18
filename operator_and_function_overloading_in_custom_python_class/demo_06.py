class Favority:
    def __init__(self, favority, user):
        self.favority = list(favority)
        self.user = user
    
    def __len__(self):
        return len(self.favority)

    def __getitem__(self,key):
        return self.favority[key]

favority = Favority(['machine leanring','deep learning','reinforcement leanring'],'mike')
print(favority[0]) #machine leanring
print(favority[-1])#reinforcement leanring