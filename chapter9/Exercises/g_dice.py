from random import randint 

class Die:
    """Class for a die"""
    
    def __init__(self, sides = 6):
        """generates an x sided die"""
        
        self.sides = sides
        
    def roll_die(self):
        
        """Prints a randomly generated number on the die """
        
        print("\nThe rolled number is:")
        print(randint  (1, self.sides))      

gambling_time = Die(6)
gambling_time.roll_die()
gambling_time.roll_die()
gambling_time.roll_die()

gambling_buddy = Die(10)
gambling_buddy.roll_die()
gambling_buddy.roll_die()
gambling_buddy.roll_die()

all_the_money_is_gone = Die(20)
all_the_money_is_gone.roll_die()
all_the_money_is_gone.roll_die()
all_the_money_is_gone.roll_die()
