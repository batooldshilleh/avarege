student_heights = input("input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
i = 0
c=0
for b in (student_heights):
    c+=b
    i+=1
avg = c/i
print(round(avg,2))

