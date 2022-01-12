#AverageHeight
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#CalculateSumofHeights
sum_of_height = 0
for height in student_heights:
  sum_of_height += height
#print(sum_of_height)

#CalculateTotalNoofStudents
no_of_student = 0
for student in student_heights:
  no_of_student += 1
#print(no_of_student)

#CalculateAvgHeight
average_height = round(sum_of_height/no_of_student)
print(average_height)