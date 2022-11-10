print("Enter your grade point")
grade = int(input())
if grade >= 90 and grade <= 100:
    print("A")

else:
    if grade >= 80 and grade <= 89:
        print("B")
    elif grade >= 70 and grade <= 79:
        print("C")

    elif grade < 70:
        print("F")
    else:
        print("Enter grade point less than or equal 100")
