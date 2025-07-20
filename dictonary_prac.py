students_grades={"Yoni":100,"Idan":89,"Eitan":99}
students_grades["Gal"]=55
students_grades["Idan"]=88

average=sum(students_grades.values())/len(students_grades)

print(average)

removed_student=students_grades.pop("Gal")

def is_found(name):
    for key in students_grades.keys():
        if(key==name):
            return True
    return False
print(is_found("Yoni"))
#או
name="Emil"
if name in students_grades:
    print("True")
else:
    print("False")
