#Create a calendar
#Zamafuze Ngcobo
#18 March 2023

month = input("Enter the name of a month (e.g. January, ..., December): \n")
day = input("Enter the start day (1 for Monday, ..., 7 for Sunday): \n")

if  (month == "January" or month == "February" or month =="March" or month == "April" or month == "May" or month=="June" or month=="July" or month=="August" or month=="September" or month=="October" or month=="November" or month=="December"):
    if month == "January" or month == "March" or month=="July" or month=="May" or month=="August" or month=="October" or month=="December": #31 
        
        day = {
            "Sunday": 0,
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6
        }        
        
        
        
        
        print(month)
        print("Mo Tu We Th Fr Sa Su")
        n=1
        
        for b in range(1,day):
            print("  ",end=" ")
        for c in range(n,n+8-day): 
            if 1<=c<=9:
                    print("",c, end=" ")
            else:
                    print(c,end=" ")
        print()
        n= n + 8 - day
        
        
        for a in range(5):
            for i in range(n,n+7):
                if i<=31:
                    if 1<=i<=9:
                        print("",i , end=" ",)
                else:
                    print(i,end=" ")
            print()
            n+=7
        
        
    elif month =="April" or month == "June" or month=="September" or month=="November": #30
        print(month)
        print("Mo Tu We Th Fr Sa Su")
        n=1
        
        for b in range(1,day):
            print("  ",end=" ")
        for c in range(n,n+8-day):
            if 1<=c<=9:
                    print("",c , end=" ",)
            else:
                    print(c,end=" ")
        print()
        n= n + 8 - day
        
        
        for a in range(5):
            for i in range(n,n+7):
                if i<=30:
                    if 1<=i<=9:
                        print("",i , end=" ",)
                    else:
                        print(i,end=" ")
            print()
            n+=7
        
    elif month == "February": #28
        print(month)
        print("Mo Tu We Th Fr Sa Su") 
        print("")
        n=1
        
        for f in range(1,day):
            print("  ",end=" ")
        for g in range(n,n+8-day):
            if 1<=g<=9:
                    print("",g, end=" ",)
            else:
                    print(g,end=" ")
        print()
        n= n + 8 - day
        
        
        for a in range(5):
            for i in range(n,n+7):
                if i<=28:
                    if 1<=i<=9:
                        print("",i , end=" ",)
                    else:
                        print(i,end=" ")
            print()
            n+=7
        
        
        
else:
    print("Invalid calendar: you have either entered an incorrect month name or start day.")