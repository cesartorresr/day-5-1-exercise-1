# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# First define the variables of sum and count for later sum and count in the loop
sum_height = 0
count = 0
for n in student_heights:
   sum_height += n
   count += 1
average = sum_height / count
print(round(average))

