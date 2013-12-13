from categories import Formatter

class TwoFormatter(Formatter):

    def formatText(self, text):
        """Takes plain text, returns HTML"""
        return text * 2
        
    def activate(self):
        print 'activating!'

    def deactivate(self):
        print 'deactivating!'
