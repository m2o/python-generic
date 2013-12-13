from categories import Formatter

class ThreeFormatter(Formatter):

    def formatText(self, text):
        """Takes plain text, returns HTML"""
        return text * 3
