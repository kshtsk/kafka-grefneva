from pytest import mark
from unittest.mock import Mock, patch

from grecha.checkers.regex import RegexChecker
from grecha.checkers.example import ExampleChecker


class TestExampleCheck(object):
    @patch("requests.get")
    @mark.parametrize('response_ref', [
            (True, "multiline\ntext with example string\nhere\n"),
            (False, "multiline\ntext with xample string\nhere\n"),
            (True, "example string in the beginning"),
            (True, "one more example"),
            (False, "no e-x-a-m-p-l-e here"),
            (False, ""),
            (False, "\n"),
            (False, "\r\n"),
        ])
    def test_dockercheck(self, m_requests_get, response_ref):
        (match, text) = response_ref
        response = Mock()
        response.text = text
        response.status_code = 200
        m_requests_get.return_value = response
        checker = ExampleChecker('localhost')
        message = checker.check()
        assert (text, message.get('match')) == (text, match)

class HelloWorldChecker(RegexChecker):
    def __init__(self, url):
        RegexChecker.__init__(self, url)
        self.regex = ['hello\\s+world']


class TestHelloWorldChecker(object):
    @patch("requests.get")
    @mark.parametrize('response_ref', [
            (True, "hello world"),
            (True, "hello  world"),
            (True, "hello\tworld"),
            (True, "hello\nworld"),
            (False, "helloworld"),
        ])
    def test_check(self, m_requests_get, response_ref):
        (match, text) = response_ref
        response = Mock()
        response.text = text
        response.status_code = 200
        m_requests_get.return_value = response
        checker = HelloWorldChecker('localhost')
        message = checker.check()
        assert (text, message.get('match')) == (text, match)
