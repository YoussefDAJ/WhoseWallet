print("Welcome to 'Whose Wallet?")
print("Give me a list of names, and I will pick a person to pay")

names = input("If you are ready, please enter names sperated by a comma: \n").split(
    ", "
)

import random

randome_name = random.choice(names)
print(f"Tell {randome_name} to pay the bill")
