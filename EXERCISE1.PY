#calculator example IF,ELIF & ELSE
a=int(input("Enter the first value:"))
b=int(input("Enter the Second Value:"))
operator = input("Enter the operator(+,-,*,/):")
if operator == "+":
    print("the sum of :",a+b)
    # elif or else mein diffrence- elif udo use hundi jado jada conditions nu check karna-or hr ik condition ko
    # check karna ho- agr first condition gallt hundi ta oh dusri condition check karda
    #Else - udo use hundi jado bki sabhi if or elif conditions gallat ho.or else k pass koi condition nahi hoti
    # or je tb execute hoti hai jado if or elif condition true nahi hoti
elif operator =="-":
    print("the sum of:",a-b)
elif operator =="*":
    print("the sum of:",a*b)
elif operator =="/":
    print("the sum of:",a/b)
    # 0 k sath divide nhi hota to ye option vi add kar skte ta ki koi agr kre to error nh aaye
     # Division से पहले यह चेक करें कि denominator 0 नहीं है
    if b!=0:
         print("The division of :", a / b)
    else:
         print("Error: Division by zero is not allowed!")
else:
 print("invalid opertor.please enter on of +,-,*,/")

#  Even or Odd Checker (2 example)- ehde layi modulo check krde or eh check krn de lyi ik hi value 
# input krde bc 2 nl divide krn te agr 0 aya ta evn nhi ta odd or agr calculator lyu banna fr 2 values input krniya
c= int(input("enter the value:"))
if c % 2 == 0: # 2 de nl divide krn te equal to zero hunda ta even
    print("if the reminder is zero then print even")
else:
    print("if the reminder is 2,3,4 etc then print odd")

    # Grade Calculator
    cal=int(input("enter the number:"))
    if(cal>90):
        print("if the number is more then 90 then Grade A")
    elif (cal>80 and cal <= 90):
        print( "Grade B")
    elif (cal>70 and cal <= 80):
        print("Grade c")
    elif (cal>60 and cal <=70):
        print("Grade D")
    else:
        print("grade f")

 #password validator -exercise pending and string reverse pending/ number range checkker/find maxium of three number
# multipication table (2,4 so on) ------ string methods

# number range checker
 #nested if statement - ik if k ander ik if lga diya isko  10-50 vr lga skte hai/ ik condition check hon to vd
 # ik hr condition check karni hve ta
num= int(input("Enter the num: "))
if(num<0):
    print("number is negative")
elif(num>0):
    if(num<=10):
       print("number is b/w 1-10")
    elif(num>10 and num <=20):
       print("number is b/w 11-20")
    else:
       print("number is greator than 20")
else:
  print("number is zero")













