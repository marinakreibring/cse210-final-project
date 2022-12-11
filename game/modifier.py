"""This is Modifier class"""

from game.determiner import Determiner
from game.subject import Subject
from game.word import Word
import random

class Modifier(Word):
    """The Modifier here represents an attribute, object or adverbial modifier.
    It is a prepositional phrase which consists of a preposition, determiner and noun.
    
    The responsibility of Modifier is to choose a randon preposition, then to add
    a determiner from Determiner and noun from Subject; and create a string. 

    Attribute:
        number (int): singular (1) or plural (2)
    """
    def __init__(self):
        super().__init__()
        self.determiner = Determiner
        self.subject = Subject
        
    def _get_word(number):
           
        """First take a randomly chosen preposition from this list of prepositions. Then build and return a prepositional phrase composed of three
        words: a preposition, a determiner, and a noun.
        
        Parameter
            number: an integer that determines if the determiner and noun.

        Return: a prepositional phrase.
        
        """
        words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
        # Randomly choose and return a preposition.
        prep = random.choice(words)
                
        # compose a prepositional phrase
        # for singular form
        if number == 1:
            determiner = Determiner._get_word(1)
            noun = Subject._get_word(1)            
        # for plural form
        else:
            determiner = Determiner._get_word(2)
            noun = Subject._get_word(2)   

        prep_phrase = (prep, determiner, noun)
        return prep_phrase