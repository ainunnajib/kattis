from collections import defaultdict
project2students = defaultdict(set)
student2projects = defaultdict(set)

while True:
    s = input()
    if s == '0':
        break
    while s != '1':
        if s[0].isupper():
            project = s
            project2students[project] = set()
            student = ''
        else:
            student = s
        if project != '' and student != '':
            student2projects[student].add(project)
            project2students[project].add(student)

        s = input()

    kick = set()
    for s in student2projects:
        if len(student2projects[s]) > 1:
            kick.add(s)

    for p in project2students:
        project2students[p] -= kick

    l = []
    for p in project2students:
        l.append((-1*len(project2students[p]), p))
    l.sort()

    for x in l:
        print(x[1], -1*x[0])

    project2students = defaultdict(set)
    student2projects = defaultdict(set)
    project, student = '', ''
