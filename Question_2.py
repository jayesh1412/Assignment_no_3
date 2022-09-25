def reverse(v):
       str=" "
       for i in v:
             str = i + str 
       return str

v = "1234abcd"

print("The original string is ", end="") 
print(v)

print("The reversed string(using loops) is", end="")
print (reverse(v)) 