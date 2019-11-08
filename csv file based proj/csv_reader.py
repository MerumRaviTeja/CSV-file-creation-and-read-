import csv
l = []
with open('student_marks.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = int(columns[-1].rstrip('\n'))
        l.append(tuple(columns))
    print(l)

subject_faculty = []
with open('subject_faculty.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = columns[-1].rstrip('\n')
        subject_faculty.append(tuple(columns))
    print(subject_faculty)


