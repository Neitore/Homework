students = int(input('Enter number of students: '))
apples = int(input('Enter number of apples: '))
result = (apples // students)
left = (apples % students)
print('Apples per student: ' + str(result))
print('Apples left in basket: ' + str(left))