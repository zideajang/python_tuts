class Favority:
    def __init__(self, favority, user):
        self.favority = list(favority)
        self.user = user
    
    def __len__(self):
        return len(self.favority)

    
    


favority = Favority(['machine leanring','deep learning','reinforcement leanring'],'mike')
print(len(favority))#3