rent = int(input("enter your flat rent = "))
food = int(input("enter the ampount of food ordered = "))
electricity_spend = int(input("enter the total of electricity spend ="))
charge_per_unit = int(input("enter the charge per unit = "))
persons = int(input("enter the numbers of persons living in flat ="))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons 

print("each person will pay = ",output)