import random
class Pound:
    def __init__(self,rare=False):
        self.rare=rare
        if self.rare:
            self.value=1.25
        else:
            self.value=1.0
        self.color="gold"
        self.num_edges=1
        self.diameter=22.5#in mm
        self.thickness=3.15#in mm
        self.heads=True
    def rust(self):
        self.color="greenish"
    def clean(self):
        self.color="gold"
    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.head=choice
    def __del__(self):
        print("coin spent")
coin1=Pound()
print(coin1.color)
coin1.rust()
print(coin1.color)
coin1.clean()
print(coin1.color)
print(coin1.heads)
coin1.flip()
print(coin1.heads)
coin2=Pound(rare=True)
print(coin1.value)
print(coin2.value)