from game.terminal_service import TerminalService
from game.determiner import Determiner
from game.adjective import Adjective
from game.subject import Subject
from game.predicate import Predicate
from game.modifier import Modifier

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to get information from other classes and 
    put it together and create a sentence.

    Attributes:
        determiner (Determiner): The determiner (article, or other word)
        adjective (Adjective): the adjective
        subject (Subject): the noun
        predicate (Predicate): the verb
        modifier (Modifier): a prepositional phrase
        terminal_service: For getting user input and displaying information on the terminal.
        is_playing (boolean): Whether or not to keep playing.
    """
    
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.determiner = Determiner
        self.adjective = Adjective
        self.subject = Subject
        self.predicate = Predicate
        self.modifier = Modifier
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.sentence="" 
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            # print greeting
            self._terminal_service.write_text("\nWelcome to the fun sentence-maker!")
                    
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
                            
            # ask about another game (terminal returns answers in lower case)
            answer = self._terminal_service.read_text("\nWould you like to play again? [y/n]: ")
            if answer=="y":
                self._is_playing = True
                
            elif answer=="n":
                self._is_playing = False
                self._terminal_service.write_text("\nThank you for the game! Good bye!\n")
            else:
                self._terminal_service.write_text("Invalid responce.")
                self._terminal_service.read_text("Please answer with [y/n]: ")

    def _get_inputs(self):
        """Get the input from user.

        Args:
            self (Director): An instance of Director.
        """
        # get the number for the noun
        self.number = self._terminal_service.read_number("\nPlease choose singular or plural noun [1/2]: ")
        # get the tense for the verb
        self.tense = self._terminal_service.read_text("\nPlease choose the tense for the verb [past/present/future]: ")
                
    def _do_updates(self):
        """Gets information from Determiner, Noun, Predicate and Adjective
        to get the words.
        
        Args:
            self (Director): An instance of Director.
        """
        # give a value to every word
        # prepositional phrases (modifiers) each have 3 words, so separate them 
        self.a = self.determiner._get_word(self.number)
        self.b = self.adjective._get_word()
        self.c = self.subject._get_word(self.number)
        phrase1 = self.modifier._get_word(self.number)
        self.d = phrase1[0]
        self.e = phrase1[1]
        self.f = phrase1[2]
        self.g = self.predicate._get_word(self.number, self.tense)
        phrase2 = self.modifier._get_word(self.number)
        self.h = phrase2[0]
        self.i = phrase2[1]
        self.j = phrase2[2]
               
    def _do_outputs(self):
        """Print the sentence.

        Args:
            self (Director): An instance of Director.
        """
        # add all word's values onto one string and print the sentence through the terminal service
        self.sentence = self.a.capitalize() + " " + self.b + " " + self.c + " " + self.d + " " + self.e + " " + self.f + " " + self.g + " " + self.h + " " + self.i + " " +self.j + "."
        print()  
        self._terminal_service.write_text(self.sentence)
                    