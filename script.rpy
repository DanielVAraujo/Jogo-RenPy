﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pisquinha")
define h = Character("Husk")
define k = Character("Kai")


# The game starts here.

label start:

    
    play music "audio/headofsteal.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene campodeflores
    with fade
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Dois irmãos lutam pela liderança do clã dos lobos"

    show pisquinha at left

    p "Não quero brigar com você irmão..."

    p "Essa luta não faz sentido pra mim!"

    show husk at right

    h "Deixa de conversa mole Pisquinha!"

    h "Isso pra mim tem outro nome..."

    h "Covardia!"
    # This ends the game.

    return
