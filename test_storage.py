
"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: Runs the main menu and handles user input.
Resources: Refactored from Project 1
Date: October 30, 2026
"""

from anime import Anime
from storage import save_anime, load_anime


def test_save_and_load_anime(tmp_path):
    """Test that anime data saves and loads correctly."""
    anime = Anime("Naruto", 220)
    anime.update_progress(220)
    anime.rate_anime(9)

    test_file = tmp_path / "test_anime.json"

    save_anime([anime], test_file)
    loaded_data = load_anime(test_file)

    assert len(loaded_data) == 1
    assert loaded_data[0]["name"] == "Naruto"
    assert loaded_data[0]["total"] == 220
    assert loaded_data[0]["watched"] == 220
    assert loaded_data[0]["status"] == "Completed"
    assert loaded_data[0]["rating"] == 9