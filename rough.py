import enum
import time
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3
# print the enum member as a string
print ("The enum member as a string is : ",end="")
print (Days.Mon.value)

def yield_understading():
   yield 'understood'
   yield 'or not?'
   time.sleep(10)
   print('hello')
   # return 'its over now'
ret = yield_understading()
# print(yield_understading())
x=0
for i in yield_understading():
   print(x)
   print(i)
   
   x=x+1
  
   # print(ret)