sandwich_orders = ["Chicken","Grilled Beef","Double chicken","Veg"]
finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print (f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print ("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print ("- " + sandwich)