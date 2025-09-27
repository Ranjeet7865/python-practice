import datetime # import means kise dusri file ya library to code lena
datetime.datetime.now() # current date or time lene k liye 
current_hour=datetime.datetime.now().hour
if 5 <= current_hour <= 11:
    print("good morning")
elif 12<= current_hour <=17:
    print("GA")
elif 18<= current_hour <=21:
    print("GE")
else:
    print("gn")

# print star patteren
n = 4
for k in range (1, n+1):
    for i in range (k):
        print (k, end="")  # end means multiple lines nu ik line ch print karna
    print()    
    
    # FIND FACTORIAL OF A NUMBER
n=8
product =1 # intilize kita like kine de nl multiply karna
for i in range (1,n+1): # 1 means loop kitho start hundi, n+1 loop kithe tk chalni 8 tk 
   product= product *i # 1*1,1*2 so on and product variable name hai
print(product)

# even or odd check karna 

n = int(input().strip()) # STRIP MEANS String mein empty white space ko remove karne k liye use hota hai
if n % 2 != 0: # like agar odd hove ta 
        print ("weird")
elif (n % 2 ==0 and 2 <=  n <= 5): # agr n even hove or range 2 to 5 de viche hove ta print
        print (" Not weird")
elif (n % 2 ==0 and 6 <=  n <= 20):  # agr n even hove or range 6 to 20 de viche hove ta print
        print ("weird")
else:                                # agr n even hove or grater than 20 hove ta print
        print ("Not weired")
        
# reverse input string

d= (input()) [::-1]
print (d)

# word ko reverse karna

d = input("Enter the string: ")
words = d.split()  # String ko words mein split karo
reversed_words = [word[::-1] for word in words]  # Har word ko reverse karo
result = " ".join(reversed_words)  # Sabhi words ko join karke ek string bana lo
print(result)

# find the sum of digit

number= input("enter the no. ")
sum_of_digits = 0
for digit in number:
 sum_of_digits += int(digit)
 print(f"The sum of the digits in {number} is {sum_of_digits}.") # f-string means agar string k ander
 #variable ko directly add karna ho  to (w/o + ) apko {}- braces k ander variable likhna hai

# Check if a Number is Prime:

d= int(input("enter the nos:"))
if d ==1 :
    print("not prime")  # 1 is not a prime number
elif( d <= 1):
    print ( "not prime")  # Negative numbers are not prime
else:
    # Loop to check divisibility from 2 to (d-1) 
    # - like 11-1=10 and 2 se lekr 10 tk divide karna 11 ko
    # agr reminder 0 ata hai to not prime otherwise prime
    for i in range (2, d): 
      if d % i == 0:  # Agar number i se divide hota hai, to prime nahi
       print("Not prime")
       break  # Break loop agar prime nahi hai
    else:
     print("Prime")  # Agar loop complete ho jata hai without breaking, to prime hai

# Find the largest number
     
numbers= list(map(int,input("find largest").split())) # map,int input ko list of integers mein badal dega
# split string ko individual parts (numbers) mein tod dega, jo space se separate hain.
largest =numbers[0] #largest ko pehla number assign karo initially
for num in numbers:
        if num > largest:
            largest=num # agar current number largest se bada hai, to largest ko update karo
print("The largest number is:", largest) # string k sath variable ki value ko print krega
     
# count vowels in string

string= input("enter the a string: ").lower()
vowels= "aeiou"
count= 0 # count karn de lyi intilize kita
for char in string: # character de har string nu loop karn lyi
    if char in vowels: # agr char vowels mein hai
        count +=1 # count ko increment krega
print (f"Number of vowels : {count}") # volwels count ko print krega
# factrorial

n=5
product= 1
for j in range (1,n+1):
   product= product *j
print(product)










