def cal_percent(marks):
  totalmarks=sum(marks)
  percent=(totalmarks/ 500)*100
  return percent
  
def grad(percent):
    if percent >=80:
        return "A grade"
    elif percent >=70:
        return "B grade"
    elif percent >=60:
        return "c grade"
    elif percent >=45:
        return"D grade"
    elif percent >=33:
        return "E grade"
    else :
        return "student fail"
        
def main_marks():
    name=input("Enter your name : ")
    subjects =["English:","hindi:","science:","so.science:","maths:"]
    marks=[]
    
    for sub in subjects:
        while True :
            mark=float(input(f"Enter your marks in {sub}"))
            if mark <0 or mark>100:
                print("Enter valid marks 0 to 100")
            else :
                marks.append(mark)
                break
            
    percentag= cal_percent(marks)
    grads=grad(percentag)
    print (percentag)
    print (grads)
        
            
main_marks()