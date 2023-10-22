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

inv1 = f"\n{guest[0]}, are you free for dinner this evening?"
inv2 = f"{guest[1]}, are you free for dinner this evening"
inv3 = f"{guest[2]}, are you free for dinner this evening"
inv4 = f"{guest[3]}, are you free for dinner this evening"

print(inv1)
print(inv2)
print(inv3)
print(inv4)

msg = "\nI'm sorry, but I can only invite two individuals because the dinner table seems to be having some issues and won't arrive in time."
print(msg)

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


del(guest[0] , guest[0])

print(guest)