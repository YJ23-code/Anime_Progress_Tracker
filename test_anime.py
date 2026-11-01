"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: It runs the main menu and handles the user input
Resources: Refactored from Project 1
Date: October 30, 2026
"""

import pytest
from anime import Anime


def test_create_anime():
    """Test that a new anime has the correct starting values"""
    anime = Anime("Naruto", 220)

    assert anime.name == "Naruto"
    assert anime.total == 220
    assert anime.watched == 0
    assert anime.status == "Watching"
    assert anime.rating is None


def test_anime_progress():
    """Test that anime progress is calculated correctly""" 
    anime = Anime("Naruto", 220)

    anime.update_progress(110)

    assert anime.watched == 110
    assert anime.get_progress() == 50.0
    assert anime.status == "Watching"


def test_complete_anime():
    """Test that finishing an anime changes its status."""
    anime = Anime("Naruto", 220)

    anime.update_progress(220)

    assert anime.watched == 220
    assert anime.get_progress() == 100.0
    assert anime.status == "Completed"   


def test_rate_anime():
    """Test that a completed anime can be rated."""
    anime = Anime("Naruto", 220)

    anime.update_progress(220)
    anime.rate_anime(8)

    assert anime.rating == 8
    assert anime.status == "Completed"


def test_invalid_rating():
    """Test that ratings above 10 are rejected."""
    anime = Anime("Naruto", 220)

    anime.update_progress(220)

    with pytest.raises(ValueError):
        anime.rate_anime(15)    

