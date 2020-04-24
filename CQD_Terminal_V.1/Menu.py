#Menu#

from CGen import charater_gen


print(""" 
    DnD Charater Auto Builder (5E)
    
    By Grant Walker, April 2020
    """)

def menuscreen():
    print("""
This program will help build a basic charater for DnD,
it will randomly choose a race, class and ablity rolls,
along with the changes race and class can make

Press 1 to Start
Press 2 to Quit

""")
    menu_selection_number = input("Please select a number: ")
    try:
        menu_selection_int = int(menu_selection_number)
        print("you have selected: ", menu_selection_int)
    except ValueError:
        print(" Invalid Selection! ")
        menuscreen()

    if menu_selection_int == 1:
        charater_gen()
    elif menu_selection_int == 2:
        exit()
    elif menu_selection_int == 69:  # Keeping this for meme reasons
        print("Nice...")
        menuscreen()
    elif menu_selection_int == 42:  # Keeping this for meme reasons
        print("The ultimate answer to life, the universe and everything...")
        menuscreen()
    else:
        print("Invalid Selection! Please try again")
        menuscreen()

menuscreen()


