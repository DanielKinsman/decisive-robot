#!/usr/bin/env python

""" Unit tests for deicisiverobot.py """

import unittest
import decisiverobot

class TestDecisiveRobot(unittest.TestCase):
    """ Unit tests for DecisiveRobot class """
    
    def setUp(self):
        pass
    
    def testOr(self):
        """ Tests a simple choice between two options """
        answer = decisiverobot.answer('tofu or tempeh?')
        self.assertFalse(answer != 'tofu' and answer != 'tempeh')
            
    def testUnicode(self):
        """ Ensures unicode compliance for question answers """
        answer = decisiverobot.answer(u'tofu or tempeh?')
        self.assertFalse(answer != u'tofu' and answer != u'tempeh')    
        self.assertEqual(type(answer), unicode)
        
if __name__ == '__main__':
    unittest.main()