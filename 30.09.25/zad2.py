grades = [95, 82, 67, 54, 100, 73, 88, 42]
excellent=[]
good=[]
passs=[]
fail=[]

for grade in grades:
    if(grade>=90):
        excellent.append(grade)
    elif(grade>=70 and grade<90):
        good.append(grade)
    elif(grade>=50 and grade<70):
        passs.append(grade)
    else:
        fail.append(grade)

print(f"The excellent grades are {excellent}.")
print(f"The excellent grades are {good}.")
print(f"The excellent grades are {passs}.")
print(f"The excellent grades are {fail}.")