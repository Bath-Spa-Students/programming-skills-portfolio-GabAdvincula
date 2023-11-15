#Assume the lists numbers1 has 100 elements and numbers2 is an empty list.
#Write code that copies the values in numbers to numbers2

numbers1 = list(range(101))

numbers2 = numbers1[:]  

print("numbers2:", numbers2)