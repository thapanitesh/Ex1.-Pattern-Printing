import datetime
def gettime():
    return datetime.datetime.now()
def activities_add(client):
    if client == 1:
        choose = int(input("Enter 1 for diet & 2 for execersise:\n"))
        add_activities = input("Enter what do your perfer:\n")
        if choose == 1:
            with open("Nitesh_diet.txt", "a") as f:
                f.write(str([str(gettime())])+":"+add_activities+"\n")
            print("Sucessfully Written")
        elif choose == 2:
            with open("Nitesh_execersise.txt", "a") as f:
                f.write(str([str(gettime())])+":"+add_activities+"\n")
            print("Sucessfully Written")
    if client == 2:
        choose = int(input("Enter 1 for diet & 2 for execersise:\n"))
        add_activities = input("Enter what do your perfer:\n")
        if choose == 1:
            with open("Aashish_diet.txt", "a") as f:
                f.write(str([str(gettime())])+":"+add_activities+"\n")
            print("Sucessfully Written")
        elif choose == 2:
            with open("Aashish_execersise.txt", "a") as f:
                f.write(str([str(gettime())])+":"+add_activities+"\n")
            print("Sucessfully Written")  
    if client == 3:
        choose = int(input("Enter 1 for diet & 2 for execersise:\n"))
        add_activities = input("Enter what do your perfer:\n")
        if choose == 1:
            with open("Sudip_diet.txt", "a") as f:
                f.write(str([str(gettime())])+":"+add_activities+"\n")
            print("Sucessfully Written")
        elif choose == 2:
            with open("Sudip_execersise.txt", "a") as f:
                f.write(str([str(gettime())])+":"+add_activities+"\n")
            print("Sucessfully Written") 
def retrevie(client):
    if client == 1:
        choose = int(input("Enter 1 for diet & 2 for execersise:\n"))
        if choose == 1:
            with open("Nitesh_diet.txt") as f:
                for i in f:
                    print(i,end="")   
        elif client == 2:
            with open("Nitesh_execersise.txt") as f:
                for i in f:
                    print(i,end="")  
    if client == 2:
        choose = int(input("Enter 1 for diet & 2 for execersise:\n"))
        if choose == 1:
            with open("Aashish_diet.txt") as f:
                for i in f:
                    print(i,end="")   
        elif client == 2:
            with open("Aashish_execersise.txt") as f:
                for i in f:
                    print(i,end="")  
    if client == 3:
        choose = int(input("Enter 1 for diet & 2 for execersise:\n"))
        if choose == 1:
            with open("Sudip_diet.txt") as f:
                for i in f:
                    print(i,end="")   
        elif client == 2:
            with open("Sudip_execersise.txt") as f:
                for i in f:
                    print(i,end="")  
a = int(input("Press 1 for add_activities & 2 for retrevie:\n"))
if a == 1:
    client = int(input("Enter 1 for Nitesh, 2 for Aashish & 3 for Sudip:\n")) 
    activities_add(client)  
elif a == 2:
    client = int(input("Enter 1 for Nitesh, 2 for Aashish & 3 for Sudip:\n")) 
    retrevie(client)  

