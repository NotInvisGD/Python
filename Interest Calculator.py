while True:
    print("")
    print("Type 1 for Simple Interest!\nType 2 for Compound Interest!")

    try:
        interest_type = int(input("Enter your choice!: "))
        interest_type_name_simple_interest = "Simple Interest"
        interest_type_name_compound_interest = "Compound Interest"

        if (interest_type == 1):
            print(f"Alright, your interest type is {interest_type_name_simple_interest}!")
        elif (interest_type == 2):
            print(f"Alright, your interest type is {interest_type_name_compound_interest}!")

        principal = int(input("Enter the principal amount!: "))
        time = int(input("Enter the time (per annum): "))
        rate = float(input("Enter your rate % (do not type % after number): "))
        Simple_Interest_Itself = (principal * rate * time) / 100
        Compound_Interest_Amount = principal * ((1 + (rate / 100)) ** time)
        Compound_Interest_Itself = (Compound_Interest_Amount - principal)
        Simple_Interest_Amount = (principal + Simple_Interest_Itself)

        def simple_interest():
            print("")
            print("Calculating simple interest...")
            print(f"\tThe corresponding simple interest for your given data is: {round(Simple_Interest_Itself, 2)}")
            print(f"\tThe corresponding amount after simple interest for your given data is: {round(Simple_Interest_Amount, 2)}")

        def compound_interest():
            print("")
            print("Calculating compound interest...")
            print(f"\tThe corresponding compound interest for your given data is: {round(Compound_Interest_Itself, 2)}")
            print(f"\tThe corresponding amount after compound interest for your given data is: {round(Compound_Interest_Amount, 2)}")

        if (interest_type == 1):
            simple_interest()
        elif (interest_type == 2):
            compound_interest()
        elif (interest_type > 2 or interest_type < 1):
            print("Please enter a valid number!")

        print("")
        print("Thanks for using my program! Do you want to use it again? Type 1 for Yes, and 2 for No!")
        user_continual_choice = int(input("Enter your choice for continual!: "))

        if user_continual_choice == 1:
            continue
        elif user_continual_choice == 2:
            print("")
            print("Thanks for using the program!")
            break
        elif (user_continual_choice > 2 or user_continual_choice < 1):
            print("")
            print("Invalid choice. Exiting the program!")
            break

    except ValueError:
        print("Please enter a valid number!")
