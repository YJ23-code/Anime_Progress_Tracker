"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: It runs the main menu and handles the user input
Resources: Refactored from Project 1
Date: October 30, 2026
"""

from tracker import AnimeTracker

def show_menu():
    """Display the anime tracker menu"""
    print("\n== Anime Progress Tracker ==")
    print("1.Add anime")
    print("2.View anime list")
    print("3. Update progress")
    print("4. rate anime")
    print("5.Exit")

def main():
    """Run the anime progress tracker program"""
    tracker = AnimeTracker()

    while True:
        show_menu()
        choice = input("Choos1e an option: ")


        if choice =="1":
            name = input("Enter anime name: ")
            total = int(input("Enter total episodes: "))
            tracker.add_anime(name, total)
            print(name, "was added to your list")
        elif choice =="2":
            tracker.view_anime()

        elif choice =="3":
            name = input("Enter the anime name: ")
            episodes = int(input ("How many episodes have you watched? "))

            tracker.update_anime(name, episodes)
            print("Progress updated ")

        elif choice == "4":
            name = input("Enter the anime name: ")
            rating = int(input("Rate this anime from 1 to 10 "))

            tracker.rate_anime(name, rating)
            print("Rating saved")

        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Please choose an option from 1 to 5")

if __name__ == "__main__":
    main()
           
                   


        
        
