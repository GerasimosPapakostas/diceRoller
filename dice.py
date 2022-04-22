#dice.py
import random
from dice_faces_diagram import *
from diceroll import *

def analyze_input(input_string):
    if input_string.strip() in {"1","2","3","4","5","6"}: #remove the spaces with strip
        return int(input_string)  #return the number as integer
    else:
        print("Please give a valid number in the interval (1,6) ")
        raise SystemExit(1)




        
#User's input#
def main():    
    num_dice_in=input(" How many dices do you want to roll? [1-6] ")
    num_dice=analyze_input(num_dice_in)
    results=dice_roll(num_dice)
    print(results)
    dice_face_diagram = generate_dice_face_diagram(results)
    print(f"\n{dice_face_diagram}")

if __name__=="__main__":
    main()


