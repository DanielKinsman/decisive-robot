# Copyright 2012 Daniel Kinsman
#
# This file is part of Decisive Robot.
#
# Decisive Robot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Decisive Robot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Decisive Robot.  If not, see <http://www.gnu.org/licenses/>.

"""Provides answers to questions in the guise of a surly,
   human loathing robot"""

import re
import random

REG_OPTIONS = re.compile(r'\bor\b|,', re.IGNORECASE)
REG_QUESTION = re.compile(r'\?')
REG_REMOVE = re.compile(r'\b(which|what|when|where|how|should|i|we)\b', \
                        re.IGNORECASE)

INSULTS = ['MEATBAG', 'MEATBAG', 'MEATBAG', 'MEATBAG', 'FLESH GOLEM',
            'JUICE SACK', 'HUMAN']

def answer(question):
    """Provides an answer to a question,
       randomly choosing between the different options."""
    if not(type(question) is str or unicode):
        raise TypeError('question argument should be a string')
      
    #remove "Should I" etc
    question = REG_REMOVE.sub('', question)

    #split on ',' 'OR', 'or', 'Or', 'oR'
    matches = REG_OPTIONS.split(question)
    choices = list()

    for candidate in matches:
        # remove question marks and leading/trailing whitespace
        candidate = candidate.strip()
        candidate = REG_QUESTION.sub('', candidate)

        # Strings like 'or,' or ',,,' will produce empty candidates.
        if len(candidate) > 0:
            choices.append(candidate)

    return random.choice(choices)

def snarkyanswer(question):
    """Provides an answer to a question,
       using a randomly choosing between the different options,
       while talking in ALL CAPS and calling you MEATBAG"""

    vanilla = answer(question)
    return vanilla.upper() + ", " + random.choice(INSULTS)