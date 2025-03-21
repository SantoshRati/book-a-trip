def goa():
    print("Thanks for Choosing GOA This package is 10k per person")
    print("Do you want to book...?\n")
    print("1. Yes")
    print("2. No")
    Choose_your_choice = int(input("Enter the number:\n"))
    if Choose_your_choice == 1:
        per_person = 10000
        fullname = input("enter your name:\n ")
        age = int(input("enter your age:\n "))
        if age < 18:
            print("sorry you cant book the trip")
            return
        else:
            print("eligible")
        no_of_persons = int(input("enter no of person:\n"))
        total_amount = per_person*no_of_persons
        if total_amount >= 50000:
            offer = 5000
            payable_amount = total_amount - offer
            print(f"Hi {fullname} your booked goa trip your bill more than 50k so 5000 less and you have to pay: rs{payable_amount}")
        else:
            print(f"Hi {fullname} your booked goa trip you have to pay: rs{total_amount}")
    else:
        main()

def mysore():
    print("Thanks for Choosing mysore This package is 15k per person")
    print("Do you want to book...?\n")
    print("1. Yes")
    print("2. No")
    Choose_your_choice = int(input("Enter the number:\n"))
    if Choose_your_choice == 1:
        per_person = 50000
        fullname = input("enter your name:\n ")
        age = int(input("enter your age:\n "))
        if age < 18:
            print("sorry you cant book the trip")
            return
        else:
            print("eligible")
        no_of_persons = int(input("enter no of person:\n"))
        total_amount = per_person*no_of_persons
        if total_amount >= 50000:
            offer = 5000
            payable_amount = total_amount - offer
            print(f"Hi {fullname} your booked mysore trip your bill more than 50k so 5000 less and you have to pay {payable_amount}")
        else:
            print(f"Hi {fullname} your booked mysore trip you have to pay: rs{total_amount}")
    else:
        main()
    
def tirupati():
    print("Thanks for Choosing tirupati This package is 20k per person")
    print("Do you want to book...?\n")
    print("1. Yes")
    print("2. No")
    Choose_your_choice = int(input("Enter the number:\n"))
    if Choose_your_choice == 1:
        per_person = 20000
        fullname = input("enter your name:\n ")
        age = int(input("enter your age:\n "))
        if age  <18:
            print("sorry you cant book the trip")
            return
        else:
            print("eligible")
        no_of_persons = int(input("enter no of person:\n"))
        total_amount = per_person*no_of_persons
        if total_amount >= 80000:
            offer = 5000
            payable_amount = total_amount - offer
            print(f"Hi {fullname} your booked tirupati trip your bill more than 50k so 5000 less and you have to pay {payable_amount}")
        else:
            print(f"Hi {fullname} your booked tirupati trip you have to pay: rs{total_amount}")
    else:
        main()
    
def delhi():
    print("Thanks for Choosing delhi This package is 30k per person")
    print("Do you want to book...?\n")
    print("1. Yes")
    print("2. No")
    Choose_your_choice = int(input("Enter the number:\n"))
    if Choose_your_choice == 1:
        per_person = 30000
        fullname = input("enter your name:\n ")
        age = int(input("enter your age:\n "))
        if age  <18:
            print("sorry you cant book the trip")
            return
        else:
            print("eligible")
        no_of_persons = int(input("enter no of person:\n"))
        total_amount = per_person*no_of_persons
        if total_amount >= 100000:
            offer = 10000
            payable_amount = total_amount - offer
            print(f"Hi {fullname} your booked delhi trip your bill more than 50k so 5000 less and you have to pay {payable_amount}")
        else:
            print(f"Hi {fullname} your booked delhi trip you have to pay: rs{total_amount}")
    else:
        main()

def main():
    print("***WELCOME TO OUR TRAVELS***")
    print("1. Goa")
    print("2. Mysore")
    print("3. Tirupati")
    print("4. Delhi")
    print("5. Exit")
    print("Please choose trip you want to book now")
    Trip_Number = int(input("Enter your choice:\n"))
    if Trip_Number == 1:
        goa()
    elif Trip_Number == 2:
        mysore()
    elif Trip_Number == 3:
        tirupati()
    elif Trip_Number == 4:
        delhi()
    elif Trip_Number == 5:
        return
    else:
        print("Please enter valid number")
main()



