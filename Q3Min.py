no_of_seconds=int(input("Enter no of Seconds:"))

if(no_of_seconds<60):
    print("no of seconds",no_of_seconds,"seconds")

else:
    e=no_of_seconds//60
    f=no_of_seconds%60

    print(e,"minutes", f,"seconds")