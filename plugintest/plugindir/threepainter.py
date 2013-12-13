from categories import Painter

class ThreeFormatter(Painter):

    def paintText(self, text):
        """Takes plain text, returns HTML"""
        return '@paint '+text * 3
