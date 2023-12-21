print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10,12 or 15?"))
total_people = int(input("How many people to split the bill?"))
tip_percent = tip/100
total_tip_amount = bill*tip_percent
total_bill = bill+total_tip_amount
per_person_bill = total_bill/total_people
final_amount_per_person = round(per_person_bill, 2)  
print(f"Each person has to pay ${final_amount_per_person}")