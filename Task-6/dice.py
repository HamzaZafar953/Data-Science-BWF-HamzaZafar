from random import randint

class Dice:
	
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
		
		
        #Prints a random number between 1 and the number of sides
        
        result = randint(1, self.sides)
        print(f"Rolling a {self.sides}-sided dice: {result}")


# Create a 6-sided dice and roll it 10 times

print("Rolling a 6-sided dice 10 times:")
six_sided_dice = Dice()
for _ in range(10):
    six_sided_dice.roll_dice()
    

# Create a 10-sided dice and roll it 10 times

print("\nRolling a 10-sided dice 10 times:")
ten_sided_dice = Dice(sides=10)
for _ in range(10):
    ten_sided_dice.roll_dice()


# Create a 20-sided dice and roll it 10 times

print("\nRolling a 20-sided dice 10 times:")
twenty_sided_dice = Dice(sides=20)
for _ in range(10):
    twenty_sided_dice.roll_dice()

