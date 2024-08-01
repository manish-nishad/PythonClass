def percent(marks):
    obtained_marks = sum(marks)
    print("Obtained Marks by the student is :",obtained_marks)
    percentage = (obtained_marks/500) *100
    return percentage



def grade(percentage):
    if percentage >= 90:
        return "Grade A"
    elif percentage >= 80:
        return "Grade B"
    elif percentage >=70:
        return "Grade C"
    elif percentage >=50:
        return "Grade D"
    elif percentage>=33:
        return "Grade F"
    else:
        return "The student is fail "
    


def marks():
    name=str(input("Enter your name"))
    subjects = ["English","Hindi", "Maths", "Science","Socail science"]
    mark = []
    for i in subjects:
        while True:
            i=float(input(f"Enter the marks of {i} subject :"))
            if i < 0 or i > 100:
                print("Please enter the marks between 0 to 100 ")
            else:
                marks.append(i)
                break


a=percent(marks)
b=grade(percent)

