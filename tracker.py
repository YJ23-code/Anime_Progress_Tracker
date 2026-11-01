"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: Manages the anime list and saves progress.
Resources: Refactored from Project 1.
Date: October 30, 2026
"""


from anime import Anime
from storage import save_anime, load_anime

class AnimeTracker:
    """Manages a collection of anime objects"""

    def __init__(self):
        """Create an anime list and load saved data."""
        self.anime_list = []

        saved_data = load_anime()

        for item in saved_data:
            anime = Anime(item["name"], item["total"])
            anime.update_progress(item["watched"])

            if item["rating"] is not None:
                anime.rate_anime(item["rating"])

            self.anime_list.append(anime)

    def add_anime(self, name, total):
        """Add a new anime if it isnt already in the list"""
        if self.find_anime(name) is not None:
            raise ValueError("That anime is already in your list")

        new_anime = Anime(name, total)
        self.anime_list.append(new_anime)
        save_anime(self.anime_list)
        return new_anime    

    def find_anime(self, name):
        """Find an anime by name, ignoring capitalization."""
        for anime in self.anime_list:
            if anime.name.lower() == name.strip().lower():
                return anime

        return None


    def view_anime(self):
        """Display all anime and their progress."""
        if not self.anime_list:
            print("Your anime list is empty.")
            return

        print("Your anime list:")

        for anime in self.anime_list:
            print(
                anime.name, "-",
                anime.watched, "/", anime.total, "-",
                anime.status, "-",
                anime.get_progress(), "%"
            )

            if anime.rating is not None:
                print("Rating:", anime.rating, "/10")

    def update_anime(self, name, episodes):
        """Update the progress of an anime in the list"""
        anime = self.find_anime(name)
        if anime is None:
            raise ValueError("Anime not found")

        anime.update_progress(episodes)
        save_anime(self.anime_list)
        return anime 


    def rate_anime(self, name, rating):
        """Save a rating for a completed anime"""
        anime = self.find_anime(name)

        if anime is None:
            raise ValueError("Anime not found")

        anime.rate_anime(rating)
        save_anime(self.anime_list)
        return anime           