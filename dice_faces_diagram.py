import random
from diceART import*
def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces

def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGH):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows

def generate_dice_face_diagram(dice_values):
    #Generate a list of dice faces from diceART#
    dice_faces = _get_dice_faces(dice_values)
    #Generate a list containing the dice faces rows#
    dice_faces_rows=_generate_dice_faces_rows(dice_faces)
    #Generate Header with the word "RESULTS" centered#
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width,"~")
    dice_faces_diagram= "\n". join([diagram_header]+ dice_faces_rows)
    return dice_faces_diagram

