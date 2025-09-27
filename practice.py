print ("hello")
a=123
a1=3
print(a+a1) # concetenate islye hua kyuki data types same hai like no. hai
print (type(a)) # type check karna int ,str etc.
a= complex(8,2) #complex
print(a)
x=float(1) # int convert to float- & change so more int,complex
print(x)

for y in "apple":# loop thru letters like single word in single line
 print(y)

 #b = "ritu" length
 #print(len(b))

dict= {"name":"ritu" ,"last name":"maan" ,"education":"bca"}
print(dict)

# operators used - like make calculator
a=15
b=5
print(a+b)
print(a-b)
print(a* b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# type casting means convert karna string etc ko data type ch
C="2"
D="3"
# CONVERT TO INT
print (int(C)+ int(D)) # pheala string value ko int mein krega fr plus krega
string="15"
number= 7
string_number=int(string)
sum=number+string_number
print("the sum of both number is:",sum)

# user input
# a=input()- blank vi chd skde  ya fr  string vi fill kr skde/ input de vich string hi anda agr tuc no. laina ta int likh k input lai skde
# a=int(input("enter your age"))
a=input("enter my name:")
#print(a) ya fr
print("my name is",a)

# slicing string
nm="harry"
print(nm[-4:-2])

#strings are immutable..existing string ko chng nhi krega or nhi string create krega
a="Ritu !!! !!!"
print(a.upper())
print(a.lower())
# R.STRIP- Trailing letters delete krn lyi
print(a.rstrip("!")) # delete krde hai traling characters nu like- !, (white space-del. krn lyi a.strip). etc etc only backend(trailing character) ko delete krta front wale ko nhi 
# replace word
print(a.replace("Ritu","Maan")) # REPLACE THE Character
# split- agr space chahiye to -(" ") agr delete karni ho to blank
print(a.split(" ")) 

# CAPITALIZE
blogwithritu="introduction to css"
print(blogwithritu.capitalize())

# center
print(blogwithritu.center(40))
# count- karna ki kini vr lkhiya print(a.count("ritu"))
# endswith - like end ko check karna ki (!!!), anything kis k sath ho rha output true or false mein & same as startwith()
print(blogwithritu.endswith("to",11,15))
# find() - find krna accurance or agr nhi hoyi ta return karuga -1 or agr hooyi ta count krke duc di 5 ayi
print(blogwithritu.find("duchh"))
#index("duchh") - hamara program error de kar exit kar jaye to use index method
#isalnum -isalphanumeric string hai k nhi (A-Z,a-z, 0-9. if any other characters or punctuation are present then return false)
#isalpha - (A-Z,a-z.if any other characters or punctuation are present then return false)
#islower- check krega ki sare letters lower case mein hai k nhi- agr hai to true nhi to false
#isprintable 
# isspace- check karda ahite space hai k nahi(true0false return)
#istitle() first latter of each word ko capatalized krne k liye title ko 
#swapcase() lower case ko uppercase or upper case ko lower case
#title()- capatalizes each letter of the word








