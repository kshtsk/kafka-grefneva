from .regex import RegexChecker

class ExampleChecker(RegexChecker):
    def __init__(self, url):
        RegexChecker.__init__(self, url)
        self.regex = ['example']

