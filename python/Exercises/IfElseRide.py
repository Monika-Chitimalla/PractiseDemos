print("Welcome to the Roller Coster")
height=int(input("Please enter your height in cms:"))

if height>120:
    print("Congratulations! You can take a ride!")
    age=int(input("What is your age?"))
    if age<=18 and age>12:
        print("Your ticket price is $7!")
    elif age<=12:
        print("Your ticket prce is $5")
    else:
        print("Your ticket price is $12")   
        
else:
    print("Sorry, You will have to grow taller before you take a ride!")
