"""Provides answers to questions in the guise of a surly,
   human loathing robot"""

import re
import random

#split on ',' 'OR', 'or', 'Or', 'oR'
REG_OPTIONS = re.compile(r'\Wor\W|,', re.IGNORECASE)
REG_QUESTION = re.compile(r'\?')

def answer(question):
    """Provides an answer to a question,
       using a randomly choosing between the different options."""
    if not(type(question) is str or unicode):
        raise TypeError('question argument should be a string')
      
    matches = REG_OPTIONS.split(question)
    choices = list()
    
    for candidate in matches:
        candidate = candidate.strip()
        candidate = REG_QUESTION.sub('', candidate)
        choices.append(candidate)
        
    return random.choice(choices)