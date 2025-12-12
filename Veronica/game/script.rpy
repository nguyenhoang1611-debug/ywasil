# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("emo guy place holder")
define n = Character("narrator")
define m = Character("Mother")

transform slightleft:
    xalign 0.25
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
<<<<<<< HEAD
  
   
=======
    show mother at right with moveinright
    show emo guy place holder at left with moveinleft
    
>>>>>>> d1f3dc12f5bb1d7d29cd11e5bdb1607b30c7484f
    # This ends the game.
   

    return
