"""
Program: Anime Progress Tracker
Author: Yasir
Purpose: Saves and loads anime data using JSON files.
Resources: Refactored from Project 1
Date: October 30, 2026
"""

import pytest
from tracker import AnimeTracker


@pytest.fixture
def test_tracker(tmp_path, monkeypatch):
    """Create a tracker using a temporary JSON file."""
    import storage
    import tracker as tracker_module

    test_file = tmp_path / "test_anime_data.json"

    original_save = storage.save_anime
    original_load = storage.load_anime

    monkeypatch.setattr(
        tracker_module,
        "save_anime",
        lambda anime_list: original_save(anime_list, test_file)
    )

    monkeypatch.setattr(
        tracker_module,
        "load_anime",
        lambda: original_load(test_file)
    )

    return AnimeTracker()


def test_add_anime(test_tracker):
    """Test that a new anime is added to the tracker."""
    test_tracker.add_anime("Naruto", 220)

    assert len(test_tracker.anime_list) == 1
    assert test_tracker.anime_list[0].name == "Naruto"
    assert test_tracker.anime_list[0].total == 220


def test_duplicate_anime(test_tracker):
    """test that duplicate anime names arre rejected"""
    test_tracker.add_anime("Naruto", 220)
    with pytest.raises(ValueError):
        test_tracker.add_anime("Naruto", 220)

        assert len(test_tracker.anime_list) == 1


def test_update_anime(test_tracker):
    """Test that anime progress updates correctly."""
    test_tracker.add_anime("Naruto", 220)

    test_tracker.update_anime("Naruto", 110)

    anime = test_tracker.find_anime("Naruto")
    assert anime.watched == 110
    assert anime.get_progress() == 50.0
    assert anime.status == "Watching"


def test_rate_anime(test_tracker):
    """Test that a completed anime can be rated."""
    test_tracker.add_anime("Naruto", 220)

    test_tracker.update_anime("Naruto", 220)
    test_tracker.rate_anime("Naruto", 9)

    anime = test_tracker.find_anime("Naruto")

    assert anime.rating == 9
    assert anime.status == "Completed"    