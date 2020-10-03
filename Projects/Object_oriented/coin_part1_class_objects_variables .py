class Pound:
    value=1.0
    color="gold"
    num_edges=1
    diameter=22.5# in millimeter
    thicknes=3.15#in millimeter
    heads=True
coin1=Pound()
print(type(coin1))
print(coin1.value)
print(coin1.color)
coin1.color="greenish"
print(coin1.color)
coin2=Pound()
print(coin2.color)
coin1.value=1.2
print(coin2.value)
