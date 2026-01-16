name=["Amit","John","Rishabh","Eshan","Aman"]
rollnumber=[1,2,3,4]
cgpa={"Amit":9.1,"John":8.5,"Rishabh":9.3,"Eshan":9.1}
subject={"MAT":1001,"CSE":1201,"CHY":1234,"EEE":1456,"ENG":1765}
while True:
     print("1.Take Attendance for Students:")
     print("2.Record Student's CGPA:")
     print("3.Display Student Details:")
     print("4.Want to see Subject code:")
     print("5.want to Add new Student:")
     print("6.Want to give cgpa to new Student:")
     print("7.want to remove Student:")
     print("8.Exit")
     input1=int(input("Enter your choice by selecting number between(1-8):"))

     if input1==1:
        for i in name:
          attendence=input(f"Is {i} present today? (y/n):")
          if attendence=="y":
              print(f"{i} is present today.")
          elif attendence=="n":
              print(f"{i} is absent today.")
     elif input1==2:
       student_name=input("Enter Student's name to record CGPA:")
       if student_name in name:
            student_cgpa=float(input("Enter CGPA:"))    
            cgpa[student_name]=student_cgpa
            print("CGPA recorded successfully.")
       else:
            print(f"no student in class with name {student_name}")    
            
     elif input1==3:
      for n, r in zip(name, rollnumber):
             print(f"Name: {n}, Roll No: {r}")

     elif input1==4:
        code=input("Enter Subject for which you want subject code:")
        if code in subject:
          print(f" Subject code for {code} is {subject[code]}")
        else:
         print("No Subject is present in our course with this name ")      

     elif input1==5:
      a=input("Enter a New Student Name:")    
      b=int(input("Enter a New Roll number for new student:")) 
      name.append(a)
      rollnumber.append(b)
      print(f"{a} with rollnumber {b} is added to our class list")
      print(f"{a} You are most welcome in your new class")
      print(name)
      print(rollnumber)
     elif input1==6:
        print(f" total student list : {name}") 
        c=input("Enter a name of new student :")
        if c in name:
           d=float(input("Enter a cgpa  scored by {c}:"))
           cgpa.update({c:d})
           print(f"{c} has scored cgpa of {d}")
           print("cgpa has been stored")
        else:
           print(f"We have no student named {c}")   
     elif input1==7: 
        e=input("Enter a name of student you want to remove :") 
        if e in name:
           name.remove(e)     
           print(f"student with named {e} has been removed from attendence record")
        else:
           print(f" there is no student named {e} in our class")   
     elif input1==8:
        print("Class is over student ")    
        f="GOOD BYE"
        print(f.center(50))
        break


            
            
        
