#Write a python program with nested decision structures that perform the following: 
#If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2

amount1 = 30
amount2 = 50

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print("Greater amount is:", amount1)
        elif amount2 > amount1:
            print("Greater amount is:", amount2)
        else:
            print("Both are equal:", amount1)
    else:
        print("amount2 does not fall below 100.")
else:
    print("amount 1 does not exceed ten.")