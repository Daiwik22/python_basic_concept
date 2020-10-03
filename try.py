class Dog:
    def __init__(self):
      self.color="brown"

    def wash(self):
        self.color="white"
        return self.color


dog1=Dog()
print(dog1.color)

color_new=dog1.wash()
print(color_new)