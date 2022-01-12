#HeadsorTails
import random

random_toss = random.randint(0,1)
print(random_toss)
if random_toss == 0:
  print(f"Tails")
else:
  print(f"Heads")