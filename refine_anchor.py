import scraper

"""
Pass the program an href= anchor from BeautifulSoup and will correctly format it into an FQDN

anchors = [x.get('href') for x in BeautifulSoup(requests.get("http://google.com").text, 'html.parser').findAll('a')]
for an_anchor in self.get_anchors():
    anchor = self.test_anchor(an_anchor)
    if anchor is not False and anchor is not None:
        self.add_formatted_anchor(anchor)
return self.get_formatted_anchors()
        
call using:

spider = RefineAnchor("irongeek.com")
formatted_anchors = spider.main()
print(formatted_anchors)
"""


class RefineAnchor:

    url = None
    anchor = None
    formatted_anchors = None

    def __init__(self, an_url):
        self.url = an_url
        self.anchor = ""
        self.formatted_anchors = []

    def set_url(self, an_url):
        self.url = an_url

    def get_url(self):
        return self.url

    def set_anchor(self, an_anchor):
        self.anchor = an_anchor

    def get_anchor(self):
        return self.anchor

    # Test if anchor contains in-scope URL
    def test_anchor_in_scope(self, an_anchor):
        if self.get_url() in an_anchor:
            return True
        else:
            return False

    # If anchor doesn't contain any URL
    def test_anchor_has_scope(self, an_anchor):
        domain = self.get_url().split('.')[1]
        if len(an_anchor.split('.')) == 4:
            temp_anchor = an_anchor.split('.')[2][0:len(domain)]
        elif len(an_anchor.split('.')) == 3:
            temp_anchor = an_anchor.split('.')[2][0:len(domain)]
        elif len(an_anchor.split('.')) == 2:
            temp_anchor = an_anchor.split('.')[1][0:len(domain)]
        elif len(an_anchor.split('.')) < 2 or len(an_anchor.split('.')) > 4:
            return False
        if domain == temp_anchor:
            return True
        else:
            return False

    # Test if anchor contains HTTP schema
    def test_anchor_has_schema(self, an_anchor):
        if an_anchor[0:4] == 'http':
            return True
        else:
            return False

    def test_anchor(self):
        # If anchor is not in scope, reject it if test_anchor_has_scope() is True
        in_scope = self.test_anchor_in_scope(self.get_anchor())

        # If anchor has no scope, add the scope (url)
        has_scope = self.test_anchor_has_scope(self.get_anchor())

        # If anchor has no schema, add the schema ('http://')
        has_schema = self.test_anchor_has_schema(self.get_anchor())

        if in_scope and has_scope and has_schema:
            # Do nothing, the anchor is complete
            return self.get_anchor()

        if not in_scope and has_scope and has_schema:
            # Reject it, it's out of scope
            an_anchor = False
            return an_anchor

        if in_scope and has_scope and not has_schema:
            # Add the HTTP schema to it
            return 'http://' + self.get_anchor()

        if not in_scope and not has_scope and not has_schema:
            # Add the schema and the URL to it
            if self.get_anchor()[0] == '/':
                return 'http://' + self.get_url() + self.get_anchor()
            elif self.get_anchor()[0] != '/':
                return 'http://' + self.get_url() + '/' + self.get_anchor()

