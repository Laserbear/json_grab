from burp import IBurpExtender
from burp import IProxyListener

class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks( self, callbacks):
        # your extension code here
         self._callbacks = callbacks
        
        # set our extension name
        callbacks.setExtensionName("JSON Grab")
        
        # obtain our output stream
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        
        # register ourselves as a Proxy listener
        callbacks.registerProxyListener(self)

    #
    # implement IProxyListener
    #

    def processProxyMessage(self, messageIsRequest, message):
        self._stdout.println(
                ("Proxy request to " if messageIsRequest else "Proxy response from ") +
                entropy.find_entropy(message.getMessageInfo().getResponse()))