import urllib
from urllib.parse import urlparse

class Operation:

    # init method or constructor
    def __init__(self,
                 path):

        parseResult = urlparse(path)

        self.path = parseResult.path
        self.query = parseResult.query
        self.operation = parseResult.path
        self.scheme = parseResult.scheme

        if (self.query != ""):
            parseQuery = urllib.parse.parse_qs(parseResult.query)
            self.id = parseQuery.get("id")[0]