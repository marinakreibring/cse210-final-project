"""This is a code for adjective class"""
import random
from game.word import Word

class Adjective(Word):
    """The responsibility of a Adjective is to choose a random adjective from the list.
    
    Attributes:
        none
    """

    def __init__(self) -> None:
        super().__init__()
                  
    def _get_word():
        """Return a randomly chosen adjective.
        
        Parameters:
            none.
        Return: a randomly chosen adjective.
        """
        # Create a list of strings 
        words = ["beautiful", "funny", "hungry", "sad", "sleepy", "cute", "fast", "purple", "white", "yellow", "strong", "long", "orange", "tall", "interesting", "green", "slow", "bright", "delicious", "angry"]
        # Call the random.choice function which will choose a noun
        word = random.choice(words)
        return word