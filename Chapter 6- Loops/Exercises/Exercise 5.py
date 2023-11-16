sandwich_orders = ["Chicken","Pastrami","Grilled Beef","Pastrami","Double chicken","Veg","Pastrami"]
finished_sandwiches = []
print ("The deli has run out of Pastrami")
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print (f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print ("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print ("Pastrami")