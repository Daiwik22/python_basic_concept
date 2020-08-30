import random
#Default health of a person
health=50
health_potion=random.randint(25,50)
health= health + health_potion
print(health)
#1,2,3 difficulty level of game
#Higher the difficulty -lesser the potion

difficulty=2
#Health pottion magically generates health
health_potion=int(random.randint(25,50)/difficulty)