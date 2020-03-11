# Course: CS 30
# Period: 1
# Date created: 2020/02/12
# Date last modified: 2020/03/11
# Name: Kate Pepper
# Desrcription: A set of lists for a Clue RPG

"""A list of all of the suspects of the murder"""
# Original suspect list
suspects = ['Evelyn Finch', 'George Brown', 'Madeline Brown', 'Stephen Turner']
print(" ")
print(suspects)
# Additional suspects added to the list
suspects.append('Chantal Steele')
suspects.insert(2, 'Justin Jones')
print(" ")
print(suspects)
# A sentence including each suspect
for suspect in suspects:
    print(f"\n{suspect.title()} is a suspect in this murder case.")
# Reordered list of suspects
print("\nHere's an alphabetical list of suspects:")
print(sorted(suspects))
print("\nHere's the list normally:")
print(suspects)
# Number of suspects in case
print("\nHere is the number of suspects in this case:")
print(len(suspects))

"""A list of all of the potential murder weapons"""
# Original list of murder weapons
weapons = ['knife', 'poison', 'gun', 'crowbar', 'axe', 'rope', 'bat', 'rifle']
print(" ")
print(weapons)
# Revisions to the list of murder weapons
del weapons[-1]
print(" ")
print(weapons)
weapons.remove('bat')
print(" ")
print(weapons)
# Reordering the murder weapons
weapons.reverse()
print(" ")
print(weapons)
# Murder weapons written out in a sentence
for weapon in weapons:
    print(f"\nThe {weapon.title()} is a potential murder weapon.")

"""A list of potential rooms where the murder took place"""
# Original list of rooms
rooms = ['library', 'kitchen', 'bathroom', 'dining room', 'bedroom', 'office']
print(" ")
print(rooms)
# A sentence with each room
for room in rooms:
    print(f"\nThe murder may have taken place in the {room.title()}.")
# Removing and printing the room where the murder took place
murder_room = rooms.pop()
print(f"\nThe murder took place in the {murder_room.title()}.\n")
print(rooms)
# Reorganising the list of rooms
rooms.sort()
print(" ")
print(rooms)
