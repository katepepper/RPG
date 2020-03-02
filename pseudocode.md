# Start: game
    # Start: main menu
    # End: main menu

# Start: main menu
    # Input: "what do you want to do?"
    # Casewhere:
        # "rules", Start: rules
        # "background", Start: background
        # "controls", Start: controls
        # "start", Start: menu
    # End Casewhere:
# End: main menu

# Start: rules
    # Print: the rules of the game
# End: rules

# Start: background
    # Print: the background information on characters and the dead body
# End: background

# Start: controls
    # Print: a list of all the controls a person can use in the game
# End: controls

# Start: menu
    # Print: "welcome to the menu"
    # Input: "what would you like to do?"
    # Casewhere:
        # "map", Start: map
        # "suspect", Start: suspect
        # "guess", Start: guess
    # End Casewhere:
# End: menu
