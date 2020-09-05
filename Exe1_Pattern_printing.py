#pattern printing
# input = n interger 
# boolean = True or False
# True for n=5 
# *
# **
# ***
# ****
# False for n=5 integer
# ****
# ***
# **
# *
n = int(input("Enter the number:\n"))
Boolean = bool(int(input("choose 1 or 0:\n")))
if Boolean == True:
    for i in range(n):
        for j in range(i):
            print("*",end="")
        print()
elif Boolean == False:  
    for i in range (n):
        for j in range(n-i):
            print("*",end="") 
        print()   
