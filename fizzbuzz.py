#bir eded daxil edin 
eded = int (input("bir eded daxil edin:"))
#ededin 3 yada 5 bunusmesi yoxlayiriq 
if eded%3==0 and eded%5==0:
 print ("FizzBuzz")
elif eded%3==0:
 print ("Fizz")
elif eded%5==0:
 print ("Buzz")
elif eded%3!=0 and eded%5!=0:
 print ("eded")
