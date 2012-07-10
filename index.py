#!/usr/bin/env python

""" Pyjamas file for the index.html """

import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.HTML import HTML
from pyjamas import Window
import pyjamas.ui.KeyboardListener
from pyjamas.ui.CSS import StyleSheetCssFile
from pyjamas.JSONService import JSONProxy

class IndexHtml(object):
    """ The landing page for decisive robot """
    
    def __init__(self):
        self.remote = None
        self.question = None
        self.button = None
        self.answer = None
    
    def onModuleLoad(self):
        """ Constructs the page, called when it is first loaded """
        self.remote = DataService()
        
        StyleSheetCssFile('style.css')
        
        panel = HorizontalPanel()
        
        self.question = TextBox()
        self.question.setName("textBoxFormElement")
        self.question.addKeyboardListener(self)
        panel.add(self.question)

        self.button = Button("ask", self.ask)
        panel.add(self.button)
        
        self.answer = HTML(StyleName='answerstyle')
        panel.add(self.answer)
        
        RootPanel().add(panel)
        
    def ask(self):
        """ Contacts the json rpc service to 
            get an answer to the user's question """
        params = {'question': self.question.getText()}
        self.remote.sendRequest('answer', params, self)
        
    def onKeyDown(self, sender, keycode, modifiers):
        """ Submits the question when the user hits enter """
        if(keycode == pyjamas.ui.KeyboardListener.KEY_ENTER):
            self.ask()
    
    def onKeyUp(self, sender, keycode, modifiers):
        """ Nothing we need to handle here """
        pass
    
    def onKeyPress(self, sender, keycode, modifiers):
        """ Nothing we need to handle here """
        pass
    
    def onRemoteResponse(self, response, request_info):
        """ Called when we get an asynchronous response from
            the json rpc service """
        #good stuff in request_info.method, request_info.id
        self.answer.setHTML('<blockquote>' + response + '</blockquote>')
        
    def onRemoteError(self, code, errobj, request_info):
        """ Handles any errors received from the rpc service """
        Window.alert("There was a problem talking to the robot")

     
class DataService(JSONProxy):
    """ Simple proxy to the decisive robot json service """
    def __init__(self):
        JSONProxy.__init__(self, 'service/')

    
if __name__ == '__main__':
    pyjd.setup("index.html")
    app = IndexHtml()
    app.onModuleLoad()
    pyjd.run()