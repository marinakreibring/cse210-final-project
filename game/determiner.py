"""This is a code for Determiner class"""
import random
from game.word import Word

class Determiner(Word):
    """A determiner is an article ("the", "a") or
    a word like "one", "some", "many".
    If number == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    "some", "many", or other words.
    
    Attributes:
        number (int): singular (1) or plural (2)
    """
    def __init__(self) -> None:
        super().__init__()        

    def _get_word(number):
        """Return a randomly chosen determiner.

        Parameter
           number (int): singular (1) or plural (2).
           
        Return: a randomly chosen determiner.
        """
        if number == 1:
            words = ["a", "one", "the"]
        else:
            words = ["some", "several", "many", "the", "two", "ten", "five" ]

        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word
