from .regex import RegexChecker

class ExampleChecker(RegexChecker):
    """Example Checker Class

    Checks contents of the web page text including 'example' string in any place.
    """
    def __init__(self, url):
        RegexChecker.__init__(self, url)
        self.regex = ['example']

