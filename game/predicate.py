"""This is a code for Predicate class"""
import random
from game.word import Word

class Predicate(Word):
    """A predicate is a verb. 
    The responsibility of a predicate is to accept given number and tense form.
    There is a list of verbs for each form, so that we can just choose
    a random word from any list (without modifications).
    
    Attribute:
        tense (str): past, future or present.
    """
    
    def __init__(self) -> None:
        super().__init__()
           
    def _get_word(number, tense):
        """Return a randomly chosen verb depending on the tense and number.
        
        Parameters: 
            number: an integer that determines if the returned verb is single or plural.
            tense: a string that determines the if verb is "past", "present" or "future".
        Return: a randomly chosen verb.
        """
        # Create a list of strings 
        if tense=="present" and number==1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes", "drives", "sings", "dances", "stands", "swims", "shines", "draws", "plays", "reads"]
        elif tense=="present" and number==2:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write", "drive", "sing", "dance", "stand", "swim", "shine", "draw", "play", "read"]
        elif tense=="past":
            words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote", "drove", "sang", "danced", "stood", "swam", "shone", "drew", "played", "read"]
        elif tense=="future":
            words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write", "will drive", "will sing", "will dance", "will stand", "will swim", "will shine", "will draw", "will play", "wll read"]
         # Call the random.choice function which will choose a verb
        word = random.choice(words)
        return word