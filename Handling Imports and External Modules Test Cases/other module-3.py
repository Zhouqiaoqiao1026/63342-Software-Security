#Module import alias error

# my_module.py Custom module
def sum(a:int, b:int) -> int:
 return a+b

#Main program
import my_module as wrong_alias

a = 1
b = 2
x = mp.sum(a,b) # 'mp' is undefined here
assert x == 3