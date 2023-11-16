pet1 = {'Kind':"Dog","Owner":"Luffy"}
pet2 = {'Kind':"Tiger","Owner":"John"}
pet3 = {'Kind':"Cat","Owner":"Sanji"}

pets = [pet1, pet2, pet3]

for pet in pets:
    kind = pet['Kind']
    owner = pet['Owner']
    print (f"The {kind} is owned by {owner}.")