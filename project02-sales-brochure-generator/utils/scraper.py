import requests
from bs4 import BeautifulSoup

class Fetch_website:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        self.title = (
            self.soup.title.string
            if self.soup.title
            else "No title found"
        )
        if self.soup.body:
            for tag in self.soup.body(["script", "style", "img", "input"]):
                tag.decompose()
            self.text = self.soup.body.get_text(
                separator="\n",
                strip=True
            )
        else: 
            self.text = ""