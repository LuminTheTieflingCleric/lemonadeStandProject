from customer_class import Customer

def customer_check(recipe):
    customer=Customer()
    attributes=customer.get_customer_attributes()
    sweetness_pref=attributes["sweetness"]
    ice_pref=attributes["ice"]
    price_limit=attributes["price"]

        
    if recipe["ice"] > ice_pref:
        return False
    
    if abs(recipe["lemons"]-recipe["sugar"]) < sweetness_pref:
        return False
    
    if recipe["price"] < price_limit:
        return False
    
    return True

recipe = {
    "lemons": 2,
    "sugar": 4,
    "ice": 1,
    "price": 1.5
}

for _ in range (1,50):
    print(customer_check(recipe))