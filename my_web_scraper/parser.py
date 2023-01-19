from bs4 import BeautifulSoup

class Parser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_data(self):
        # Extract data from the HTML using BeautifulSoup
        # and return it as a dictionary
        pass
