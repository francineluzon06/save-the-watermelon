Tests for logic.py functions.

from src.logic import display_word

def test_display_word():
    secret = "apple"
    guessed = {"a", "p"}
    assert display_word(secret, guessed) == "a p p _ _"
