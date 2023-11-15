#Write a python program that takes courses marks as input and then calculates average of all the courses. 
#After calculating the average, calculate the percentage of a student using total marks.
#Assume the total of all the courses marks is 500 or take the total marks from the user as input.


course1 = float(input("Course 1 marks: "))
course2 = float(input("Course 2 marks: "))

average_marks = (course1 + course2 ) / 5

total_marks = float(input("Enter the total marks: ")) 
percentage = (average_marks / total_marks) * 100

print(f"The average of all courses is: {average_marks:.2f}")
print(f"The percentage of the student is: {percentage:.2f}%")