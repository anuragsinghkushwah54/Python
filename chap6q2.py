student_marks={"hindi":"0","english":"0","maths":"0","science":"0"}
student_marks["hindi"]=int(input("please enter hindi marks"))
student_marks["english"]=int(input("please enter english marks"))
student_marks["maths"]=int(input("please enter maths marks"))
student_marks["science"]=int(input("please enter science marks"))
sum=int(student_marks.get("hindi"))+int(student_marks.get("english"))+int(student_marks.get("maths"))+int(student_marks.get("science"))
print(student_marks)
if(sum>160):
    if(int(student_marks.get("hindi"))>33 and int(student_marks.get("english"))>33 and int(student_marks.get("maths"))>33 and int(student_marks.get("science")>33)):
      print("you are pass")
else:
    print("you are fail")        


