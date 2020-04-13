import requests

BITLY_SHORTER_URL = "https://api-ssl.bitly.com/v4/shorten"


class BitlyException(Exception):
    def __init__(self, payload):
        super(BitlyException, self).__init__("Can't create short link.")
        self.payload = payload


class Bitly(object):
    def __init__(self, token, domain=None):
        if not token:
            raise ValueError("Token is empty.")

        self.token = token
        self.domain = domain or ""

    def shorten(self, url):
        if not url:
            raise ValueError("URL is empty.")

        response = requests.post(
            BITLY_SHORTER_URL,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            json={"domain": self.domain, "long_url": url,},
        )

        try:
            data = response.json()
        except:
            data = {"message": response.text, "status": response.status_code}

        if response.status_code == 200:
            return data.get("link", url)

        raise BitlyException(data)
