# Problem 5
#In lab03_p5.py we want to use the random module to generate a random number between 1 and 1212 (inclusive). We want to do so by importing the  random module using an alias called rand and using the randrange function. The code given has several problems. Identify the problems and what changes need to be made to make this code behave as expected. Fix the code to achieve the desired result.

import random
rand = random
random = rand.randrange(0, 1212)

print(random)