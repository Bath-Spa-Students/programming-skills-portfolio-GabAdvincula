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



del(guest[1])
guest.insert(2,'Mark')

inv1 = f"\n{guest[0]}, are you free for dinner this evening?"
inv2 = f"{guest[1]}, are you free for dinner this evening?" 
inv3 = f"{guest[2]}, are you free for dinner this evening?"
inv4 = f"{guest[3]}, are you free for dinner this evening?"

print(inv1)
print(inv2)
print(inv3)
print(inv4)

