 # BREAK OR COUNTINUE- breake means loop completly stop or continue means lteration skp and next iteration start
for i in range (11):
    if (i==10): # jithe tuc stop karna chahnde ho
        break   # jistrah hi i equal to 10 ho jayegi vaise hi bhar nikl jayega agge ki execute nahi ho gyi
    print ("5*",i+1,"=",5*(i+1))  # 5*,i+1 left side line or 5*i+1 right side line-i+1 intilize karna like jitho start krna hai
# same use for while loop
#i = 0
#while i < 10:  # yahaan loop 10 tak chalega
    #print("5 *", i + 1, "=", 5 * (i + 1))
    #i += 1  # har baar i ko increment karna hai
    # brake use for while loop
    #i = 0
#while True:  # infinite loop start ho gaya, eh udo use hunda jado tuc continue loop bananai hai or 
# uske ander break condition nu manage karna
    #if i == 10:  # jab i 10 ho jaye toh loop ko break kar do
       # break
    #print("5 *", i + 1, "=", 5 * (i + 1))
    #i += 1

    # continue
for i in range (10):
    if i== 5:  
        continue # ehde ch 5 nu skip kar dega or next value print ho jayegi
    print (i)

# FUNCTION TOPIC --- sepcific kmm nu krn lyi likhiya janda,Function ko baar-baar use kiya ja sakta hai, 
# bina code ko dubara likhe. Jab function ko call karte hain, toh uska Function ko baar-baar use kiya ja sakta hai,
#  bina code ko dubara likhe. Jab function ko call karte hai.toh uska code execute hota hai 
# aur result return kar sakta hai.code execute hota hai aur result return kar sakta hai.

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
def isGrater (a, b):
    if (a>b):
        print("first no. is grater")
    else:
        print("second no. is grater")

def isLesser (a,b):
    pass        # pass means function ko vad mein excute karugi hold karna
    
a = 5
b = 3
#gmean1 = (a*b)/(a+b)
#print (gmean1) # simple hai lekin baar calculate nhh karn di jgh te function use krta
calculateGmean (a,b)
isGrater (a,b)
c = 8 
d = 5
#gmean2 = (c*d)/(c+d)
#print(gmean2)
calculateGmean (c,d)
isGrater (c,d)
# function arguments & return satement
# def average(a,b):
# default arguments
def average(a=9, b=1):
    print("the avg is ", (a+b)/2)
    #average(4,6)
    average(a=9) #b ki value default(khudse) li lega
#keyword arguments, required arguments,
#  variable arguments
def average1(*numbers):
    #print(type(numbers)) - tuples
    sum=0
    for i in numbers:
        sum = sum+i
        print("average is:",sum/len(numbers))
        average1(5,6,7,1)









