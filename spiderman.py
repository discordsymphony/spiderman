import scraper
import refine_anchor
import sys

"""
Input: An url to start spidering from.
Output: Prints all valid urls
"""


class Spiderman:

    url = None
    scraper = None
    anchors = None
    formatted_anchors = None

    def __init__(self, an_url):
        self.url = an_url
        self.scraper = scraper.Scraper('http://' + self.url)
        self.anchors = []
        self.formatted_anchors = []

    def set_url(self, an_url):
        self.url = an_url

    def get_url(self):
        return self.url

    def set_scraper(self, a_scraper):
        self.scraper = a_scraper

    def get_scraper(self):
        return self.scraper

    def set_anchors(self):
        self.anchors = self.scraper.main()

    def get_anchors(self):
        return self.anchors

    def add_formatted_anchor(self, formatted_anchor):
        self.formatted_anchors.append(formatted_anchor)

    def get_formatted_anchors(self):
        return self.formatted_anchors

    def main(self):
        self.anchors = self.scraper.main()
        for anchor in self.anchors:
            refined_anchors = refine_anchor.RefineAnchor(self.get_url())
            refined_anchors.set_anchor(anchor)
            anchor = refined_anchors.test_anchor()
            if anchor is not False and anchor is not None and anchor not in self.get_formatted_anchors():
                print(anchor)
                self.add_formatted_anchor(anchor)
                # Start iterating through list of URLs
                try:
                    self.scraper.set_scrape_url(anchor)
                    self.main()
                except KeyboardInterrupt:
                    sys.exit()
        return self.get_formatted_anchors()


if __name__ == "__main__":
    print("============================")
    print("====== Spiderman v1.0 ======")
    print("============================")
    print("[*] Enter one url in the format of 'google.com'.")
    print("[!] Please don't enter the http schema, append any slashes or subdomains.")
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("[!] Usage: python3 spiderman.py google.com")
    elif len(sys.argv) == 2:
        print("\n")
        sys.setrecursionlimit(10**6)
        url = sys.argv[1]
        spiderman = Spiderman(url)
        spiderman.main()
