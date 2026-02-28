def main():
    while True:
        try:
            bill = float(input("Enter the bill amount: "))
            tip_percent = float(input("Enter the tip percentage: "))
            people = int(input("Enter the number of people: "))

            if bill < 0:
                print("Bill amount cannot be negative.\n")
                continue

            if tip_percent < 0:
                print("Tip percentage cannot be nagative.\n")
                continue

            if people <= 0:
                print("Number of people must be atleast 1,\n")
                continue

            tip = bill * (tip_percent / 100)
            total_bill = bill + tip
            per_person = total_bill / people

            print("\n **** Bill Summary **** ")
            print(f"Tip amount: ${tip:.2f}")
            print(f"Total bill: ${total_bill:.2f}")
            print(f"Each person should pay: ${per_person:.2f}")

            break

        except ValueError:
            print("Invalid input. Please enter numeric value only.\n")

        except ZeroDivisionError:
            print("Cannot divide by zero. Number of people must be atleast 1.\n")

if __name__ == "__main__":
    main()