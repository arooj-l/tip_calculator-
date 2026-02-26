

bill = float(input("enter the bill amount: "))
percent_amount = float(input("enter the percent amount: "))
people_num = int(input("Enter the num of people: "))

while True:
 try:
   tip = bill * (percent_amount/100)
   total_bill = bill + tip
   per_person = total_bill/people_num
   
   print("your amount to pay per person is: ", per_person)
   break
 except ValueError:
    print("Enter the valid number")
    