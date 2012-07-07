#!/usr/bin/env python

import unittest
import decisiverobot

class testDecisiveRobot(unittest.TestCase):
    def setUp(self):
        pass
    
    def testOr(self):
        answer = decisiverobot.answer('tofu or tempeh?')
        if answer != 'tofu' and answer != 'tempeh':
            self.assertFail()
    
    def testUnicode(self):
        answer = decisiverobot.answer(u'tofu or tempeh?')
        if answer != u'tofu' and answer != u'tempeh':
            self.assertFail()
            
        self.assertEqual(type(answer), unicode)
        
if __name__ == '__main__':
    unittest.main()