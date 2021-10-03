'''
Jeffrey Driskill
CS101L
Fall21 - M - 7-9:30
'''

print('*'*4,'Welcome to the LAB grade calculator!','*'*4)
name = input('\nWho are we calculating grades for? ==> ')
lab_grd = int(input('\nEnter the Labs grade? ==> '))
if lab_grd > 100:
    lab_grd = 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
elif lab_grd < 0:
    lab_grd = 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
exam_grd = int(input('\nEnter the EXAMS grade? ==> '))
if exam_grd > 100:
    exam_grd = 100
    print('The exam value should have been 100 or less. It has been changed to 100.')
elif exam_grd < 0:
    exam_grd = 0
    print('The exam value should have been zero or greater. It has been changed to zero.')
attend_grd = int(input('\nEnter the Attendance grade? ==> '))
if attend_grd > 100:
    attend_grd = 100
    print('The attendance value should have been 100 or less. It has been changed to 100.')
elif attend_grd < 0:
    attend_grd = 0
    print('The attendance value should have been zero or greater. It has been changed to zero.')
weight_grd = (exam_grd * .2) + (lab_grd * .7) + (attend_grd * .1)
if weight_grd >= 90:
    lett_grd = 'A'
elif weight_grd >= 80:
    lett_grd = 'B'
elif weight_grd >= 70:
    lett_grd = 'C'
elif weight_grd >= 60:
    lett_grd = 'D'
else:
    lett_grd = 'F'
print('\nThe weighted grade for {} is {}'.format(name,weight_grd))
print('\n{} has a letter grade of {}'.format(name,lett_grd))
print('\nThanks for using the Lab grade calculator!')