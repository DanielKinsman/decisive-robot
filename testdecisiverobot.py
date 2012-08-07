#!/usr/bin/env python

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

""" Unit tests for deicisiverobot.py """

import unittest
import decisiverobot
import random

class TestDecisiveRobot(unittest.TestCase):
    """ Unit tests for DecisiveRobot class """
    
    def setUp(self):
        # Use a known seed for the rng so that behaviour is deterministic
        random.seed(1)
        
    def testUnicode(self):
        """ Ensures unicode compliance for question answers """
        answer = decisiverobot.answer(u'tofu or tempeh?')
        self.assertEqual(type(answer), unicode)
    
    def testOr(self):
        """ Tests a simple choice between two options """
        answer = decisiverobot.answer('tofu or tempeh?')
        self.assertEqual(answer, 'tofu')
        answer = decisiverobot.answer('tofu or tempeh?')
        self.assertEqual(answer, 'tempeh')
        
    def testMultipleOptions(self):
        """ Tests a choice between many options """
        answer = decisiverobot.answer('tofu, tempeh, tvp or telekinesis?')
        self.assertEqual(answer, 'tofu')
        random.seed(7)
        answer = decisiverobot.answer('tofu, tempeh, tvp or telekinesis?')
        self.assertEqual(answer, 'tempeh')
        random.seed(5)
        answer = decisiverobot.answer('tofu, tempeh, tvp or telekinesis?')
        self.assertEqual(answer, 'tvp')
        random.seed(6)
        answer = decisiverobot.answer('tofu, tempeh, tvp or telekinesis?')
        self.assertEqual(answer, 'telekinesis')

    def testShouldI(self):
        """ Ensures that the words 'should I' is removed from answers """
        answer = decisiverobot.answer(u'Should I eat tofu or tempeh?')
        self.assertEqual(answer, u'eat tofu')

    def testShouldWe(self):
        """ Ensures that the words 'should we' is removed from answers """
        answer = decisiverobot.answer(u'Should we eat tofu or tempeh?')
        self.assertEqual(answer, u'eat tofu')

    def testShouldIan(self):
        """ Ensures that only the 'should' is removed 'should ian' """
        answer = decisiverobot.answer(u'Should Ian eat tofu or tempeh?')
        self.assertEqual(answer, u'Ian eat tofu')

    def testShouldWesley(self):
        """ Ensures that only the 'should' is removed 'should wesley' """
        answer = decisiverobot.answer(u'Should wesley eat tofu or tempeh?')
        self.assertEqual(answer, u'wesley eat tofu')
        
    def testOrWithComma(self):
        """ Ensures that having an 'or' next to a comma doesn't produce
            empty options """
        answer = decisiverobot.answer(u', or or or, tofu or, tempeh?')
        self.assertEqual(answer, 'tofu')
        answer = decisiverobot.answer(u', or or or, tofu or, tempeh?')
        self.assertEqual(answer, 'tempeh')

if __name__ == '__main__':
    unittest.main()