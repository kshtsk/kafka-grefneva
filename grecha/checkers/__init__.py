import requests
import time

class BasicChecker:
    """
    Basic Site Checker
    """
    regex = []
    def __init__(self, url):
        self.url = url


    def __repr__(self):
        return f'[url={self.url}]'

    def match(self, text):
        """
        Overload this method if you need extra site checking.
        """
        return None


    def check(self):
        """
        Checks site availability and returns message dict, which ontains following records:

        :key url:       site webpage address being checked
        :key match:     match results, defaults to None, `match` method should be
                        overrided if it is needed an extra page checking.
        :key date:      the check timestamp in format 'DD-mm-YYYY HH:MM:SS'
        :key status:    http response status code or None if the site is unavailable

        """
        print(f"Checking {self}")
        match = None
        try:
            response = requests.get(self.url)
            match = self.match(response.text)

            response_status = response.status_code
        except requests.exceptions.ConnectionError:
            response_status = None
        strdate = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())

        message = dict(
            url=self.url,
            status=response_status,
            match=match,
            date=strdate,
        )
        return message
