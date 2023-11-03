#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

guest= [ 'Angelo' , 'Simon' , 'Johnlloyd' , 'Luke']

inv1 = f"{guest[0]}, are you free for dinner this evening?"
inv2 = f"{guest[1]}, are you free for dinner this evening?" 
inv3 = f"{guest[2]}, are you free for dinner this evening?"
inv4 = f"{guest[3]}, are you free for dinner this evening?"
inv5 = f"\nUnfortunately, {guest[2]} cant join us for dinner."

print(inv1)
print(inv2)
print(inv3)
print(inv4)
print(inv5)

#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

del(guest[1])
guest.insert(2,'Mark')

#Print a second set of invitation messages, one for each person who is still in your list.
inv1 = f"\n{guest[0]}, are you free for dinner this evening?"
inv2 = f"{guest[1]}, are you free for dinner this evening?" 
inv3 = f"{guest[2]}, are you free for dinner this evening?"
inv4 = f"{guest[3]}, are you free for dinner this evening?"

print(inv1)
print(inv2)
print(inv3)
print(inv4)

