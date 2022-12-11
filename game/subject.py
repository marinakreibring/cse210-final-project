"""This is a code for Subject class"""
import random
from game.word import Word

class Subject(Word):
    """The responsibility of a Subject is to choose a random noun,
    according to singular or plural number.

    Attributes:
        number (int): singular (1) or plural (2).
    """

    def __init__(self) -> None:
        super().__init__()        
                
    def _get_word(number):
        """Return a randomly chosen noun.
        If number == 1, this function will return singular noun. 
        If number==2, the noun will get ending "s".
   
        Parameter:
            number: an integer.
        Return: a randomly chosen noun.
        """
        # Create a list of strings 
        words = ["bird", "boy", "car", "cat", "dog", "girl", "rabbit", "restaurant", "snake", "truck", "crocodile", "lantern", "river", "house", "book", "train", "tree", "lamp", "bottle", "tiger"]
        # Call the random.choice function which will choose a noun
        word = random.choice(words)
        # if the word is plural
        if number==2:
            word = word+"s"
        return word