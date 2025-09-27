#if ELSE Statements
a= int(input("enter your age:"))
print("your age is :",a)
#conditional operatores
# >,<, >=, <=, ==, !=
# print (a>18) -input dita main 20 or o/p ayi true
# print(a<=18) ----------------------o/p-False
# print(a==18) ----------------------o/p-False
# print(a !=18) ---------------------o/p-true
if(a>18):
    print("you can drive")
else:
    print("you can not drive")
    appleprice =10
    budget=200
    #if(appleprice <= budget): isvad else lagana eh 1st example haior 2 e.g ch if,elif,else
    if(budget-appleprice>50): # 50 rs.apple kharidne k vd bache hai to true aagyi- 200- 1kg 10=190 bachte hai means
        # 50 se jada hai to true
        print("alexa, add 1kg apples to cart.")
    elif (budget-appleprice>70):
      print("you can buy")
    else:
     print("alexa,do not add apples to cart.")
#3 e.g
num=int(input("enter the vaule of num:"))
if(num<0):
   print("number is negative:")
elif ( num==0):
   print("number is zero")
elif(num==999):
 print("number is special")
else:
 print("number is positive")

  
# MATCH CASE- SWITCH CASE STATEMENTS MEANS IK VARIABLE HAI OR USKI MATCHING KARNA LIKE CASE MATCH KARNA
X = int(input("enter the variable to match: ")) # X is the veriable to match
match X:
# if x is 0
 case 0:         # 0 OR 4 PATTERNS HAI LIKE VALUE DITI HAI EHDI JGH KUCH HR VI LIKH JO MATCH KARWANA HOVE OTHERWISE BLNK VI CHD PRINT Krwa skde
      print ("X is zero")
      # case with if condition
 case 4 if X % 2 == 0:
      print("X % 2 ==0 and case is 4")
# Empty case with if condition
 case _ if X < 10:
      print (" X is < 10")
 case _ if X != 90:
   print("not equel to 90")
   
   # for loop ---------------- name k liye hr character,list k liye hr element
   # CHARACTER
name = 'Waheguru1313'
for a in name:
   print(a)
   # for loop mein if vi lga skte hai 
   if (a=="u"):
      print("satnam")
      if "1313" in name:
         print("waheguru ji ka khalsa, waheguru ji ki fateh")
         # list
         colors = ["red","green", "blue","white"]
for color in colors:
   print(color)
   for i in color:
      print(i)

# RANGE(start,stop,step) STEP Means gap (1,12,3)
for k in range(5):
   print(k+1)
  # for k in range(1,9):
      #print(k)

      # while loop

#i = 0 
#while (i < 3):
  # print (i)
   #i = i + 1
i= int(input("enter the number: "))
while (i<= 38): # isto vd input islyi laini,pheli input to vd exit ho jwe, agr 2nd input nhi likhi ta 1st wali chalDI REHNI jani loop
   i= int(input("enter the number: "))
   print(i)

print ("done with loop")
# decrement - means reverse counting while loop
count = 5
while ( count > 0):
   print ( count)
   count= count-1
   # else include while loop- jado condition false ho jani then print
else:
      print( "i am inside else")

      # While LOOP

      #x=10
     # while x>=10 and x <= 15:
       #  print(x)
       #  x+=2

        






      
      









