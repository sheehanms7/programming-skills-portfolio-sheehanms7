guests = ["Sabah","Sathwik","Alan"]
for name in guests :
    print (f"Hello, {name}!, Inviting you for a dinner. Would you like to join?")

guest_cant_come = "Alan"
print (f"\nUnfortunately, {guest_cant_come} cant come for dinner")

new_guest = "Johan"
guests[guests.index(guest_cant_come)] = new_guest

print ("Invitation update")
for guest in guests:
  print (f"Dear {guest}, you are invited for dinner. Would you like to come?")