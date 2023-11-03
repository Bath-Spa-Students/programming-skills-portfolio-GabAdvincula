#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.]
#Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

guest = ['Angelo', 'Simon', 'Johnlloyd', 'Luke']

inv1 = f"{guest[0]}, are you free for dinner this evening?"
inv2 = f"{guest[1]}, are you free for dinner this evening?"
inv3 = f"{guest[2]}, are you free for dinner this evening?"
inv4 = f"{guest[3]}, are you free for dinner this evening?"
inv5 = f"\nUnfortunately, {guest[2]} can't join us for dinner."

print(inv1)
print(inv2)
print(inv3)
print(inv4)
print(inv5)

del guest[2]
guest.insert(2, 'Mark')
#You just heard that Johnlloyd can’t make it to the dinner, so you need to send out a new set of invitations. You invited Mark instead.
inv1 = f"\n{guest[0]}, are you free for dinner this evening?"
inv2 = f"{guest[1]}, are you free for dinner this evening"
inv3 = f"{guest[2]}, are you free for dinner this evening"
inv4 = f"{guest[3]}, are you free for dinner this evening"

print(inv1)
print(inv2)
print(inv3)
print(inv4)
#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
msg = "\nI'm sorry, but I can only invite two individuals because the dinner table seems to be having some issues and won't arrive in time."
print(msg)

#Use pop() to remove guests from your list one at a time until only two names remain in your list. 
apology1 = f"\nI apologize {guest[0]}, but unfortunately there is only space for two persons."
inv1 = guest.pop(0)
apology2 = f"I apologize {guest[0]}, but unfortunately there is only space for two persons."
inv2 = guest.pop(0)

print(apology1)
print(apology2)

inv3 = f"\n{guest[0]},you're still invited to dinner."
inv4 = f"{guest[1]},you're still invited to dinner."

print(inv3)
print(inv4)

#Use del to remove the last two names from your list, so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program.
del(guest[0] , guest[0])
print(guest)
