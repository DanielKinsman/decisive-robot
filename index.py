#!/usr/bin/env python

import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas import Window
import pyjamas.ui.KeyboardListener

class IndexHtml(object):
    def onModuleLoad(self):
        # Create a panel to hold all of the form widgets.
        panel = HorizontalPanel()

        # Create a TextBox, giving it a name so that it will be submitted.
        self.tb = TextBox()
        self.tb.setName("textBoxFormElement")
        self.tb.addKeyboardListener(self)
        panel.add(self.tb)

        self.button = Button("ask", self.ask)
        panel.add(self.button)
        
        RootPanel().add(panel)
        
    def ask(self):
        Window.setLocation('index.html?q=' + self.tb.getText())
        
    def onKeyDown(self, sender, keycode, modifiers):
        if(keycode == pyjamas.ui.KeyboardListener.KEY_ENTER):
            self.ask()
    
    def onKeyUp(self, sender, keycode, modifiers):
        pass
    
    def onKeyPress(self, sender, keycode, modifiers):
        pass
     
    
if __name__ == '__main__':
    pyjd.setup("index.html")
    app = IndexHtml()
    app.onModuleLoad()
    pyjd.run()