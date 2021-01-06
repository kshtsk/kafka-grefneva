import re

from . import BasicChecker


class RegexChecker(BasicChecker):
    """Regex Checker
    
    Use this class as base for specific regex.
    The self.regex member should contain a list
    of regular expressions.
    
       class SomeTextChecker(RegexChecker):
           def __init__(self, url):
               RegexChecker.__init__(self, url, ['sometext'])

    The checker matches the response text if any
    of the given regular expressions get matched.
    """
    def __init__(self, url, regex=None):
        BasicChecker.__init__(self, url)
        self.regex = regex or []

    def match(self, text):
        _match = None
        for x in self.regex:
            if x:
                if re.search(x, text, flags=re.MULTILINE):
                    _match = True
                    break
                else:
                    _match = False
        return _match

    def __repr__(self):
        return f'[url={self.url} regex={self.regex}]'


class AnyChecker(RegexChecker):
    """Matches any text"""
    def __init__(self, url):
        RegexChecker.__init__(self, url)
        self.regex = ['.']

