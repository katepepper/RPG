# Course: CS 30
# Period: 1
# Date created: 2020/03/10
# Date last modified: 2020/03/12
# Name: Kate Pepper
# Desrcription: A set of dictionaries for a Clue RPG

""" A dictionary of all the characters/ suspects in the case"""
characters = {"Evelyn Finch":
                {"Age": "24", "Job": "Interior Designer", "City": "Toronto" },
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
locations = {"library": "",
            "kitchen": "",
            "bathroom": "",
            "dining room": "",
            "bedroom": "",
            "office": ""
            }

"""Print instructions for the character information"""
for key in characters:
    print("Information on ")
