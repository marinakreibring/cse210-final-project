"""This is a code for Word class"""
class Word:
    """This class is a super-class for all words used in the game.
    The responsibility of this class is to set common attributes for its subclasses.

    Attributes:
       text (str): a word
       number (int): singular (1) or plural (2)
       tense (str): past, present or future 
       
    """

    def __init__(self):
        
        self._text = ""
        self._number = self.director._get_inputs.number
        self._tense = self.director._get_inputs.tense

    def _get_word():
        pass
        

