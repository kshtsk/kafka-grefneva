import requests
import time

class BasicChecker:
    """ Basic Site Checker """
    regex = []
    def __init__(self, url):
        self.url = url


    def __repr__(self):
        return f'[url={self.url}]'

    def match(self, text):
        return None


    def check(self):
        """
        Check site availability and return message dict
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
