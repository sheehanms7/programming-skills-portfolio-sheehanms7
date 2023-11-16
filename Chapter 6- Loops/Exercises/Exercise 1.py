pizza_toppings = []

while True:
    topping = input("Enter a pizza or 'quit' to finish:")
    
    if topping.lower() == 'quit':
        break
   
 

pizza_toppings.append(topping)
print(f"{topping} will be added to your pizza.")

print ("\nYour pizza will have the following toppings ")
for topping in pizza_toppings:
    print ("- " + topping)