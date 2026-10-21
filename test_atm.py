
# ATM Simulation in Python

amount = 25000
pin = 1097
transaction = 'y'

# PIN Authentication
entered_pin = None

while entered_pin != pin:
    entered_pin = int(input("ENTER YOUR PIN NUMBER: "))

    if entered_pin != pin:
        print("PLEASE ENTER VALID PASSWORD\n")

# Menu Loop
while transaction.lower() == 'y':
    print("\n----- Welcome to ATM Service -----")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Quit")
    print("5. Change PIN")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"\nYOUR BALANCE = Rs.{amount}")

    elif choice == 2:
        withdraw = int(input("\nENTER THE AMOUNT: "))

        if withdraw <= 0:
            print("\nPLEASE ENTER A VALID AMOUNT")
        elif withdraw % 100 != 0:
            print("\nPLEASE ENTER THE AMOUNT IN MULTIPLES OF 100")
        elif withdraw > (amount - 1000):
            print("\nINSUFFICIENT BALANCE")
        else:
            amount -= withdraw
            print("\nPLEASE COLLECT YOUR CASH")
            print(f"YOUR CURRENT BALANCE = Rs.{amount}")

    elif choice == 3:
        deposit = int(input("\nENTER THE AMOUNT: "))

        if deposit <= 0:
            print("\nPLEASE ENTER A VALID AMOUNT")
        else:
            amount += deposit
            print(f"YOUR BALANCE = Rs.{amount}")

    elif choice == 4:
        print("\nTHANK YOU FOR USING OUR ATM SERVICES")
        break

    elif choice == 5:
        old_pin = int(input("\nENTER YOUR CURRENT PIN: "))

        if old_pin == pin:
            new_pin = int(input("ENTER NEW PIN: "))
            confirm_pin = int(input("CONFIRM NEW PIN: "))

            if new_pin == confirm_pin:
                pin = new_pin
                print("\nPIN CHANGED SUCCESSFULLY")
            else:
                print("\nERROR: PIN MISMATCH. TRY AGAIN.")
        else:
            print("\nINVALID CURRENT PIN")

    else:
        print("\nINVALID CHOICE")

    transaction = input(
        "\nDO YOU WISH TO HAVE ANOTHER TRANSACTION? (y/n): "
    )

print("\nTHANKS FOR USING OUR ATM SERVICE")


Bug Report / Test Cases (with PIN Change)
I

Bug Id	Bug Name	Steps to Reproduce	Expected Result	Actual Result	Status
 
ATM_001	Invalid Card	Insert invalid card	Welcome Screen
should appear	Invalid card error	Fail
ATM_002	Invalid PIN	Insert valid card → Enter
wrong PIN	Ask again until valid
PIN	Displays “Invalid
Password”	Pass
ATM_003	Invalid Account Type	Insert valid card → Enter
PIN →
Choose Withdraw
→ Select wrong account
type	Should allow
Savings/Curren t
option	Displays “Invalid
Account Type”	FAIL
ATM_004	Insufficient Balance	Balance = 5000 → Try
withdraw 6000	Should show
“Insufficient Balance”	Shows error correctly	Pass
ATM_005	Transaction Limit	Try
withdrawing > 20000
in single
transaction	Should restrict and
show limit error	Limit exceeded message	FAIL
ATM_006	Day Limit	Withdraw > 40000 in
one day	Should restrict daily
withdrawals	Day limit exceeded message	Fail
ATM_007	Invalid Denominations	Enter
withdrawal
amount not	Should reject and
show “Enter	Shows invalid
denomination message	Pass
 
		multiple of
100 (e.g. 250)	multiples of 100”		
ATM_008	Receipt Not Printed	Complete a transaction	Should print receipt	No receipt printed	Pass/Fail
ATM_009	PIN Change Mismatch	Try changing PIN →
Enter two
different new PIN values	Should reject mismatch	PIN change fails
with error	Pass/Fail


