"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: Shows the anime class for tracking episodes and ratings.
Resources: Refactored from Project 1
Date: October 30, 2026
"""

class Anime:
    """Stores information and progress for one anime"""

    def __init__(self,name,total):
        """Create an anime with its name and total episodes"""
        if not name.strip():
            raise ValueError("Anime name cannot be empty")
        if total <= 0:
            raise ValueError("Total episodes must be greater than zero")

        self.name = name.strip()
        self.total = total
        self.wacthed = 0
        self.status = "Watching"
        self.rating = None

        def update_progress(self,episodes):
            """Update watched episodes and completion status"""
            if episodes < 0 or episodes > self.total:
                raise ValueError("Episodes must be between 0 and the total")
            self.watched = episodes

            if self.watched == self.total:
                self.status ="Completed"
            else:
                self.status = "Wacthing"
                self.rating = None

                def get_progress(self):
                    """Rate an anime after all episodes are watched"""
                    if self.status != "Completed":
                        raise ValueError("You can only rate completed anime")
                    if rating < 1 or rating > 10:
                        raise ValueError("Rating must be between 1 and 10")

                    self.rating = rating
                                
    