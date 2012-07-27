#!/usr/bin/env python

""" Unit tests for deicisiverobot.py """

import unittest
import decisiverobot
import random

class TestDecisiveRobot(unittest.TestCase):
    """ Unit tests for DecisiveRobot class """
    
    def setUp(self):
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