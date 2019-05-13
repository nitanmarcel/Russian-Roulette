# Russian Roulette game made in python. The rules are simple: Each player has to press enter to pull the trigger
# and the player that hits the chambers that contains the bullet, losses!


# After the game is over the user has the option to restart the game.

import random
import os
import sys

chambers = 6
fatal_bullet = random.randint(1, chambers)

while True:
    input("Press enter to pull the trigger! ")
    if random.randint(1, chambers) == fatal_bullet:
        print("You just got served!")
        print("Game Over")
        start_again = input("Do you want to start again? (y/n): ")
        if start_again and start_again.lower()[0] == "y":
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            break
    print("You will live to see another day")
