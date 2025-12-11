# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("emo guy place holder")
define n = Character("narrator")
define m = Character("Mother")

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
    
    

    # This ends the game.


    return
