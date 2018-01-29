from burp import IBurpExtender
from burp import IHttpListener
from burp import IProxyListener
from burp import IScannerListener
from burp import IExtensionStateListener
from java.io import PrintWriter
from burp import IMessageEditorController
from entropy import find_entropy

class BurpExtender(IBurpExtender, IHttpListener, IExtensionStateListener):
    
    #
    # implement IBurpExtender
    #
    
    def	registerExtenderCallbacks(self, callbacks):
        # keep a reference to our callbacks object
        self._callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        
        # set our extension name
        callbacks.setExtensionName("JSON Grab")
        
        # obtain our output stream
        self._stdout = PrintWriter(callbacks.getStdout(), True)

        # register ourselves as an HTTP listener
        callbacks.registerHttpListener(self)
        
        # register ourselves as an extension state listener
        callbacks.registerExtensionStateListener(self)
    #
    # implement IHttpListener
    #

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
    	spice = None
    	if not messageIsRequest:
    		spice = find_entropy(self.helpers.bytesToString(messageInfo.getResponse()))
    	if spice:
        	self._stdout.print((str(spice)))


    #
    # implement IExtensionStateListener
    #

    def extensionUnloaded(self):
        self._stdout.println("Extension was unloaded")
"""
from burp import IBurpExtender
from burp import IProxyListener
from java.io import PrintWriter
from entropy import *

class BurpExtender(IBurpExtender, IProxyListener, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        # your extension code here
        self._callbacks = callbacks
        
        # set our extension name
        callbacks.setExtensionName("JSON Grab")
        
        # obtain our output stream
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        
        # register ourselves as a Proxy listener
        callbacks.registerProxyListener(self)
        callbacks.registerHttpListener(self)
    #
    # implement IProxyListener
    #

    def processProxyMessage(self, messageIsRequest, message):
    	p = find_entropy(message.getMessageInfo().getResponse())
        self._stdout.println(
                ("Proxy request to " if messageIsRequest else "Proxy response from ") +
                 find_entropy(message.getMessageInfo().getResponse().toString()))
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        self._stdout.println(
                ("HTTP request to " if messageIsRequest else "HTTP response from ") +
                messageInfo.getResponse().toString() +
                " [" + self._callbacks.getToolName(toolFlag) + "]")
"""