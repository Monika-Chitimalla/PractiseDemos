#Tip Calculator
print("Welcome to the tip Calculator.")
total_bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15?"))
num_of_people=int(input("How many people to split the bill?"))

bill_with_tip=total_bill+(total_bill*tip/100)
per_head_amount=round(bill_with_tip/num_of_people,2)
print(f"Each person should pay: ${per_head_amount}")