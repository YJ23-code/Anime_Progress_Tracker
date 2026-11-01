"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: Saves and loads anime data using JSON files.
Resources: Refactored from Project 1
Date: October 30, 2026
"""

import json
from pathlib import Path


def save_anime(anime_list, filename="anime_data.json"):
    """Save the anime list to a JSON file."""
    data = []

    for anime in anime_list:
        data.append({
            "name": anime.name,
            "total": anime.total,
            "watched": anime.watched,
            "status": anime.status,
            "rating": anime.rating
        })

    file_path = Path(__file__).resolve().parent / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_anime(filename="anime_data.json"):
    """Load anime data from a JSON file."""
    file_path = Path(__file__).resolve().parent / filename

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data
        
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Could not read the anime data file.")
        return []