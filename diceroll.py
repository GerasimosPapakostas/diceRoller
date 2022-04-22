import random
def dice_roll(num_dice):
    results=[]
    for _ in range(num_dice):
        roll=random.randint(1, 6)
        results.append(roll)
    return results