"""Provides answers to questions in the guise of a surly,
   human loathing robot"""

import re
import random

#split on ',' 'OR', 'or', 'Or', 'oR'
REG_OPTIONS = re.compile(r'\bor\b|,', re.IGNORECASE)
REG_QUESTION = re.compile(r'\?')
REG_REMOVE = re.compile(r'\b(which|what|when|where|how|should|i|we)\b', \
                        re.IGNORECASE)

INSULTS = ['MEATBAG', 'MEATBAG', 'MEATBAG', 'MEATBAG', 'FLESH GOLEM',
            'JUICE SACK', 'HUMAN']

def answer(question):
    """Provides an answer to a question,
       using a randomly choosing between the different options."""
    if not(type(question) is str or unicode):
        raise TypeError('question argument should be a string')
      
    question = REG_REMOVE.sub('', question)
    matches = REG_OPTIONS.split(question)
    choices = list()
    
    for candidate in matches:
        candidate = candidate.strip()
        candidate = REG_QUESTION.sub('', candidate)
        if len(candidate) > 0:
            choices.append(candidate)
    
    return random.choice(choices)

def snarkyanswer(question):
    """Provides an answer to a question,
       using a randomly choosing between the different options,
       while talking in ALL CAPS and calling you MEATBAG"""
       
    vanilla = answer(question)
    return vanilla.upper() + ", " + random.choice(INSULTS)