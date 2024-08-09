print ("welcome to quiz game !")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay! let's play :) ")
score = 0

answer = print ("what does os stand for ?")
print("1. os")
print("2. es")
print("3. ls")
print("4. operating system")
                
if answer.lower() == "operating system":
    print('correct!')
    score = score+1
else:
    print('incorrect!')
    print('Answer is operating system')

answer = input ("what does RAM stand for ?")
if answer.lower() == "random access memory":
    print('correct!')
    score = score+1
else:
    print('incorrect!.')
    print('Answer is random access memory ') 

answer = input ("what does cpu stand for ?")
if answer.lower() == "central processing unit":
    print('correct!')
    score = score+1
else:
    print('incorrect!')
    print('Answer is central processing unit')

answer = input ("what does GPU stand for ?")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score = score+1
else:
    print('incorrect!')   
    print('Answer is graphics processing unit') 

print("you got " + str(score) + "question correct " +  "out of 4")
print("you got " + str((score /4 ) * 100) + "% percent.")

