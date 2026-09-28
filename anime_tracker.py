"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: This shows the user the anime they are watching and can track their progress.
Date: September 27, 2026
"""
while True:
    print("===Anime Progress Tracker===")
    print("1. Add anime")
    print("2. View anime list")
    print("3. Update progress")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Add anime")
    elif choice == "2":
        print("View anime list")
    elif choice == "3":
        print("Update progress")
    elif choice == "4":
        print("Goodbye")
    else:
        print("Invalid choice")    


      
