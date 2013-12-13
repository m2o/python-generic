from yapsy.IPlugin import IPlugin

class Formatter(IPlugin):
    """Plugins of this class convert plain text to HTML"""

    name = "No Format"

    def formatText(self, text):
        """Takes plain text, returns HTML"""
        return text
        
class Painter(IPlugin):
    """Plugins of this class convert plain text to HTML"""

    name = "No Format"

    def paintText(self, text):
        """Takes plain text, returns HTML"""
        return '@paint '+text
