#FUNCTION FOR OBTAINING STUDENT DETAILS
#def details():
 #   name =str(input("Enter the name of the student :"))
def marks():
    
    while True:
        me=float(input("Enter the marks of english subject (greater than 0 ) :"))
        mh=float(input("Enter the marks of hindi subject:"))
        mm=float(input("Enter the marks of maths subject:"))
        ms=float(input("Enter the marks of science subject:"))
        mss=float(input("Enter the marks of social science subject:"))
    
        if me <0 :
            print("enter a valid marks greater than zero")
        else:
            break       

        obtained_marks = me+ mh + mm + ms + mss 
        print("Total marks obtained by the student is :", obtained_marks)
        percentage = (obtained_marks / 500 )* 100
        print(percentage)
        if(percentage >=90):
            print("Student got A grade")
        elif(percentage>=80):
            print("Student has B grade ")
        elif(percentage>=70):
            print("Student has C grade")
        elif(percentage>=60):
            print("Student has D grade")
        elif(percentage>=50):
            print("Student has F grade")
        else:
            print("Student has scored below 50 percent")

## calling the function

#details()
marks()