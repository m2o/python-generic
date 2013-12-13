from categories import Painter

class TwoPainter(Painter):

    def paintText(self, text):
        """Takes plain text, returns HTML"""
        return '@paint '+text * 2
