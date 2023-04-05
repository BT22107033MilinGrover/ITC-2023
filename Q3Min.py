#integral value for the number of seconds
no_of_seconds=int(input("Enter no of Seconds:"))
#using if to make sure number of seconds above 60 are included only after no of minutes
if(no_of_seconds<60):
    print("no of seconds",no_of_seconds,"seconds")
#else to make sure minutes and seconds are displayed properly for input higher than 60 seconds
else:
    e=no_of_seconds//60
    f=no_of_seconds%60
   print( e ,"minutes", "and", f , "seconds"
