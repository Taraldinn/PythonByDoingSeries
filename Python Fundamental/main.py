avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)


students = [
    {"name":"Rolf", "grade":(67,90,95,100)},
    {"name":"Bob", "grade":(67,90,95,100)},
    {"name":"Aldin", "grade":(67,90,95,100)},
    {"name":"Tara", "grade":(67,90,95,100)},

]

for student in students:
    name = student["name"]
    grades = student["grade"]

    print(f"student{name}")
    operation = input("Enter ' average ', 'Total' , or ' top':")


    if operation == "average":
        print(avg(grades))
    elif operation == "total":
        print(total(grades))
    elif operation == "top":
        print(top(grades))