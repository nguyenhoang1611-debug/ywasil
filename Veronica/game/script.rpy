# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("emo guy place holder")
define n = Character("narrator")
define m = Character("Mother")

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0
 
 
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "place holder bedroom.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "emo guy place holder.png" to the images
    # directory.

 
    scene bg bedroom 
    show emo guy place holder
    
    # These display lines of dialogue.

    e "i hate you momma"
    n 'said the emo emo guy place holder'
    n "all the children sing"
    e "hey bungolow bill what did you kill bungolow bill"
    m "get down here right now "
    e "........."
    n "no respond from the emo"
    n "suddenly......the mom knock the door" with hpunch # Shakes the screen for the next action
    n "actually.....she just crash the freaking door"
    show mother at center with vpunch # Shakes the screen for the next action
    
    m "why the heck you not respond to me!!!!!!!!!!!!!"
    show mother at slightright with moveinright
    show emo guy place holder at slightleft with moveinleft
    e "MOM WHY YOU ALWAYS SO HATRED AGAISNT ME?!"
    n "thing is about to took........a weird route....."
    m "your style look digusting!!!!!!!!!"
    e "SHUT UP!!!!!!!"
    m "YOU ARE OFFICALLY GROUNDED THIS WHOLE WEEK"
    e "YOU NOT LOVE ME!!!!!!!!!!!!"
    n "the mom walk out of his door.....angry"
    hide mother
    m "......." with hpunch # Shakes the screen for the next action
    show emo guy place holder
    e "that it......"
    e "i'm gonna get out of this hell holes"


    # This ends the game.
   

    return
