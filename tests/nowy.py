shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"}

pets = shop["pets"]

# for pet in pets:
#     print(pet)
# pets = shop["pets"][1]["breed"]

# def get_pets_by_breed(pet_shop, breed):
#     for pet in pets:
#         if shop["pets"] == "British Shorthair":
#             return pet
# breed_found = get_pets_by_breed(pets, "British Shorthair")
# print(breed_found)


# pets = shop["pets"][1]["breed"]
# print(pets)

# people = [
# {'name': "Tom", 'age': 10},
# {'name': "Mark", 'age': 5},
# {'name': "Pam", 'age': 7}
# ]

# def search(name):
#     for p in people:
#         if p['name'] == name:
#             return p

# name_found = search("Pam")
# print(name_found)

# def get_pets_by_breed(breed):
#     pets = shop["pets"]
#     for pet in pets:
#         if pet["breed"] == "British Shorthair":
#             return pet

# output = get_pets_by_breed("British Shorthair")
# print(output)

# def get_pets_by_breed(shop, breed):
#     pets = shop["pets"]
#     found_breed = [{"British Shorthair":[]}, {"Dalmation":[]}]
#     for pet in pets:
#         if pet["breed"] == "British Shorthair":
#             found_breed[1].append(pet["breed"])
#         elif pet["breed"] == "Dalmation":
#             found_breed[2].append(pet["breed"])
#     return found_breed
# breed = "British Shorthair"
# pets_found = get_pets_by_breed(shop, breed)
# print(pets_found)

def get_pets_by_breed(pet_shop, breed):
    pets = pet_shop["pets"]
    found_breed = []
    not_found = []
    for pet in pets:
        if pet["breed"] == "British Shorthair":
            found_breed.append(pet["breed"])
            print(found_breed)
        # if pet["breed"] == "Dalmation":
        #     not_found[0].append(pet["breed"])
        #     print(not_found)

get_pets_by_breed(shop, "Bob")