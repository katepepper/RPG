# Course: CS 30
# Period: 1
# Date created: 2020/03/10
# Date last modified: 2020/03/12
# Name: Kate Pepper
# Desrcription: A set of dictionaries for a Clue RPG

""" A dictionary of all the characters/ suspects in the case"""
characters = {
             "Evelyn Finch":
             {"Age": "24", "Job": "Interior Designer", "City": "Toronto"},
             "George Brown":
             {"Age": "33", "Job": "Doctor", "City": "Chicago"},
             "Madeline Brown":
             {"Age": "30", "Job": "Mechanic", "City": "Chicago"},
             "Stephen Turner":
             {"Age": "45", "Job": "Butcher", "City": "New York"},
             "Chantal Steele":
             {"Age": "21", "Job": "News Reporter", "City": "Vancouver"},
             "Justin Jones":
             {"Age": "54", "Job": "Plumber", "City": "Winnipeg"},
             }

""" A dictionary of all of the locations the murder may have taken place"""
locations = {
            "library": "large organised room where many books are stored",
            "kitchen": "room where food is prepared to be eaten",
            "bathroom": "place where people get rid of their bodily waste",
            "dining room": "room designed for eating in a social manner",
            "bedroom": "place where people sleep and rest",
            "office": "room designed for working and studying",
            }

"""A dictionary of all the possible murder weapons"""
weapons = {
          "knife": "A scout knife with a two inch blade",
          "poison": "A small vial of cyanide in a glass bottle",
          "gun": "A standard semi-automatic pistol",
          "crowbar": "A slightly rusted crowbar that's seen a lot of use",
          "axe": "An axe with a well worn handle and slightly dull blade",
          "rope": "A thick coarse rope that can support a lot of weight",
          }

"""Print instructions for the character information"""
for character, description in characters.items():
    print(f"\nInformation on {character}:")
    age = description["Age"]
    job = description["Job"]
    city = description["City"]

    print(f"\tAge: {age}")
    print(f"\tJob: {job.title()}")
    print(f"\tCity: {city.title()}")
print("\n")

"""Code for printing the locations information"""
for room, description in locations.items():
    print(f"\nThe {room.title()} is a {description}")
print("\n")

"""Code for printing the weapons information"""
for weapon, description in weapons.items():
    print(f"\n{weapon.title()}: {description}")
print("\n")
