# FizzBuzz - 1 se 100 tk print karna
number = 1
while number <= 100: # 1 se 100 tk chalega llop
 if number % 3 ==0 and number % 5 ==0:
      print("fizzbuzz")
 elif number % 3 ==0:
    print("fizz")
 elif number % 5 ==0:
     print("buzz")
 else:
      print(number)
 number += 1

# palindrome- kisi string or no. ko reverse kiya jaye or same rahe- like madam,121,racecar etc to palindrome

text = input("enter the text: ")
if text== text[::-1]: # orignal or reverse text ko compare kiya
    print ("palindrome")
else:
    print("not a palindrome")
    
# Count words in a string

d= input("enter the string: ").strip()
words = d.split()  # String ko spaces par split karna, jo list of words return karega
count = len(words)  # List ka length count karega, jo words ka total count hai
print("Total words in the string:", count)  # Words ka count print karna







    