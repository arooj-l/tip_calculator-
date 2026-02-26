

def main():
    bill = float(input("Enter the bill amount: "))
    tip_percent = float(input("Enter the tip percentages:" ))
    people = int(input("Enter the number of people: "))

    tip = bill * (tip_percent / 100)
    total = bill + tip
    per_person = total / people

    print("Tip amount: ", tip)
    print("Total bill: ", total)
    print("Each person should pay: ", per_person)

if __name__ == "__main__":
    main()