from bs4 import BeautifulSoup
import requests


"""
A web scraping engine - Pass it an URL in the format (http://google.com) and it will scrape all the anchors on the page.
"""


class Scraper:

    scrape_url = None

    def __init__(self, url_to_scrape):
        self.scrape_url = url_to_scrape
        self.scraped_anchors = []

    def set_scrape_url(self, scrape_url):
        self.scrape_url = scrape_url

    def get_scrape_url(self):
        return self.scrape_url

    def scrape_anchors_from_page(self):
        anchors = BeautifulSoup(requests.get(self.scrape_url).text, 'html.parser').findAll('a')
        for anchor in anchors:
            try:
                self.add_scraped_anchors(anchor['href'])
            except KeyError:
                pass

    def add_scraped_anchors(self, anchor):
        self.get_scraped_anchors().append(anchor)

    def get_scraped_anchors(self):
        return self.scraped_anchors

    def main(self):
        self.scrape_anchors_from_page()
        anchors = self.get_scraped_anchors()
        return anchors
