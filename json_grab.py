from burp import IBurpExtender
from 
class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks( self, callbacks):
        # your extension code here
         self._callbacks = callbacks
        
        # set our extension name
        callbacks.setExtensionName("JSON Grab")
        
        # obtain our output stream
        self._stdout = PrintWriter(callbacks.getStdout(), True)

        # register ourselves as an HTTP listener
        callbacks.registerHttpListener(self)
        
        # register ourselves as a Proxy listener
        callbacks.registerProxyListener(self)
    #
    # implement IHttpListener
    #

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        self._stdout.println(
                ("HTTP request to " if messageIsRequest else "HTTP response from ") +
                messageInfo.getHttpService().toString() +
                " [" + self._callbacks.getToolName(toolFlag) + "]")

    #
    # implement IProxyListener
    #

    def processProxyMessage(self, messageIsRequest, message):
        self._stdout.println(
                ("Proxy request to " if messageIsRequest else "Proxy response from ") +
                message.getMessageInfo().getHttpService().toString())