#Email validation checker using python string func
email=input("Enter the email:")  #g@g.in   ,cr7@gmail.com
k,j,d=0,0,0 # intialized k,j,d with zero
if len(email)>=6:  #checking len of email
    if email[0].isalpha():  #check if first symbol is alpha
        if "@" in email and (email.count('@')==1):#check if @ is present and it occurance "1 "time using and logic
            if (email[-3]==". ") ^ (email[-4]=="."): #check if . is present at last 3 or 4 pos using EX-or operation
                for i in email:
                    if i==i.isspace():#check whether space or not
                        k=1
                    elif i.isalpha(): 
                        if i==i.upper():#check whether input character is upper
                         j=1
                    elif i.isdigit():
                        continue
                    elif i=="_"or i=="." or i=="@":
                        continue     
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Invalid email 5!Email contain unallowed character")
                else:
                    print("Right Email")
            else:
                print("Invalid email 4! Email must contain '.'")

        else:
            print("Invalid email 3!Email must contain '@' one time ")
    else:
        print("Invalid email 2! Enter the first symbol alpha.")
else:
    print("Invalid Email 1!.Enter upto 6 character")
