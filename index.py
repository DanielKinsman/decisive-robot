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
from pyjamas.ui.HTML import HTML
from pyjamas import Window
import pyjamas.ui.KeyboardListener
from pyjamas.ui.CSS import StyleSheetCssFile
from pyjamas.JSONService import JSONProxy

class IndexHtml(object):
    def onModuleLoad(self):
        self.remote = DataService()
        
        StyleSheetCssFile('style.css')
        
        panel = HorizontalPanel()
        
        self.tb = TextBox()
        self.tb.setName("textBoxFormElement")
        self.tb.addKeyboardListener(self)
        panel.add(self.tb)

        self.button = Button("ask", self.ask)
        panel.add(self.button)
        
        self.answer = HTML(StyleName='answerstyle')
        panel.add(self.answer)
        
        RootPanel().add(panel)
        
    def ask(self):
        self.remote.sendRequest('answer', {'question': self.tb.getText()}, self)
        
    def onKeyDown(self, sender, keycode, modifiers):
        if(keycode == pyjamas.ui.KeyboardListener.KEY_ENTER):
            self.ask()
    
    def onKeyUp(self, sender, keycode, modifiers):
        pass
    
    def onKeyPress(self, sender, keycode, modifiers):
        pass
    
    def onRemoteResponse(self, response, request_info):
        #good stuff in request_info.method, request_info.id
        #Window.alert("got a response:" + response)
        self.answer.setHTML('<blockquote>' + response + '</blockquote>')
        
    def onRemoteError(self, code, errobj, request_info):
        Window.alert("got an error")

     
class DataService(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, 'service/')
    
if __name__ == '__main__':
    pyjd.setup("index.html")
    app = IndexHtml()
    app.onModuleLoad()
    pyjd.run()