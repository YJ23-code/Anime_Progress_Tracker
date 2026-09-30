"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: This shows the user the anime they are watching and can track their progress.
Date: September 27, 2026
"""
def show_menu():
    print("==Anime Progress Tracker==")
    print("1. Add anime")
    print("2. View anime list")
    print("3. Update progress")
    print("4. Rate anime")
    print("5. Exit")

anime_list = []
while True:
    show_menu()
  

    choice = input("Choose an option: ")

    if choice == "1":
        anime_name = input("Enter anime name:")
        total_episodes = int(input("Enter total episodes: "))
        anime_exists = False
        for anime in anime_list:
            if anime["name"].lower() == anime_name.lower():
                anime_exists = True
                break
        if anime_exists:
            print("That anime is already in your list.")  
        else:      

            anime = {
            "name": anime_name,
            "watched": 0,
            "total":total_episodes,
            "status": "Watching",
            "rating": None
        }
            anime_list.append(anime)
            print(anime_name, "was added to your list")
        
    elif choice == "2":
        if anime_list:
            print("Your anime list:")

            for anime in anime_list:
                progress = (anime["watched"] / anime["total"]) * 100
                print(anime["name"],"-",anime["watched"], "/", anime["total"], "-", anime["status"], "-", round(progress, 1), "%")
                if anime["rating"] != None:
                    print("Rating:", anime["rating"], "/10")
        else: 
            print("Your anime list is empty.")
        
    elif choice == "3":
        anime_name = input("Enter the anime name:")
        for anime in anime_list:
            if anime["name"].lower() == anime_name.lower():
                episodes = int(input("How many episodes have you watched?"))
                anime["watched"] = episodes
                if episodes >= anime["total"]:
                    anime["status"] = "Completed"
                else:
                    anime["status"] = "Watching"

                print("Update progress")
                break
                
        

    elif choice == "4":
        anime_name = input("Enter the anime name:")

        for anime in anime_list:
            if anime["name"].lower() == anime_name.lower():
                if anime["status"] == "Completed":
                 rating = int(input("Rate this anime from 1 to 10:"))
                 anime["rating"] = rating
                 print("Rating saved")
                else:
                 print("You can only rate completed anime")
                break    

    elif choice == "5":
        print("Goodbye!") 
        break


      
