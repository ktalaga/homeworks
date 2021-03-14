# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pet_sold):
    pet_shop["admin"]["pets_sold"] += pet_sold
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = pet_shop["pets"]
    found_breed = []
    for pet in pets:
        if pet["breed"] == breed:
            found_breed.append(pet)
    return found_breed

def find_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            return pet



def remove_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            pets.remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pets = pet_shop["pets"]
    pets.append(new_pet)


def get_customer_cash(customers):
    for c in customers:
        return customers["cash"]

def remove_customer_cash(customers, amount):
    customers["cash"] -= amount

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
        customers["pets"].append(new_pet)
        return customers["pets"]

def customer_can_afford_pet(customers, new_pet):
        if customers["cash"] >= new_pet["price"]:
            return True
        else:
            return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet not in pet_shop["pets"]:
        return 0
    amount = pet["price"]
    if pet["price"] > customer["cash"]:
        return 0

    add_pet_to_customer(customer, pet)
    pet_sold = get_customer_pet_count(customer)
    increase_pets_sold(pet_shop, pet_sold)
    remove_customer_cash(customer, amount)
    add_or_remove_cash(pet_shop, amount)

    
 
    


#         # self.assertEqual(1, get_customer_pet_count(customer))
# def get_customer_pet_count(customers):
#         # self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
# def get_pets_sold(pet_shop):
#         # self.assertEqual(100, get_customer_cash(customer))
# def get_customer_cash(customers):
#         # self.assertEqual(1900, get_total_cash(self.cc_pet_shop))
# def get_total_cash(pet_shop):
