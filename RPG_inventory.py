# A list of all of the suspects of the murder
suspects = ['Evelyn Finch', 'George Brown', 'Madeline Brown', 'Stephen Turner']
print(suspects)
suspects.append('Chantal Steele')
suspects.insert(2, 'Justin Jones')
print(suspects)
print("\nHere's an alphabetical list of suspects:")
print(sorted(suspects))
print("\nHere's the list normally:")
print(suspects)
print("\nHere is the number of suspects in this case")
print(len(suspects))

# A list of all of the potential murder weapons
weapons = ['knife', 'poison', 'gun', 'crowbar', 'axe', 'rope', 'bat','rifle']
print(weapons)
del weapons[-1]
print(weapons)
weapons.remove('bat')
print(weapons)
weapons.reverse()
print(weapons)

# A list of potential rooms where the murder took place
rooms = ['library', 'kitchen', 'bathroom', 'dining room', 'bedroom', 'office']
print(rooms)
murder_room = rooms.pop()
print(f"The murder took place in the {murder_room.title()}.")
print(rooms)
rooms.sort()
print(rooms)
