# Main Menu
while True:
    print("Main Menu")
    print("1. Add a new member to the file")
    print("2. Modify the details of an existing member")
    print("3. Display members")
    print("4. Exit")
    choice = input("Enter your choice: ")

    # Add a new member to the file
    if choice == "1":
        name = input("Enter name of the member: ")
        member_id = input("Enter member ID: ")
        member_type = input("Enter member type (Ordinary/Silver/Gold): ")
        credit_points = input("Enter credit points : ")
        with open("MEMBER", "a") as f:
            f.write(f"{name},{member_id},{member_type},{credit_points}\n")

    # Modify the details of an existing member
    elif choice == "2":
        member_id = input("Enter the member ID of the member to be modified: ")
        found = False
        with open("MEMBER", "r") as f:
            lines = f.readlines()
        with open("MEMBER", "w") as f:
            for line in lines:
                if member_id in line:
                    found = True
                    name, _, member_type, credit_points = line.strip().split(",")
                    name = input("Enter name of the member: ") or name
                    member_type = input("Enter member type (Ordinary/Silver/Gold): ") or member_type
                    credit_points = input("Enter credit points : ") or credit_points
                    f.write(f"{name},{member_id},{member_type},{credit_points}\n")
                else:
                    f.write(line)
        if not found:
            print("Member not found")

    # Display members
    elif choice == "3":
        with open("MEMBER", "r") as f:
            print(f.read())

    # Exit
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
