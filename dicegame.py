gunn = sum(list(map(int, input().split())))
emma = sum(list(map(int, input().split())))
if gunn > emma:
    print("Gunnar")
elif gunn < emma:
    print("Emma")
else:
    print("Tie")
