import enum
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
   print('hello')
   # return 'its over now'
ret = yield_understading()
# print(yield_understading())
for i in yield_understading():
   print(i)
   # print(ret)