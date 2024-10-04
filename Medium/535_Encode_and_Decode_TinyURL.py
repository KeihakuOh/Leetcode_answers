class Codec:
    def __init__(self):
        self.url_code = {}
        self.code_url = {}
        self.pool = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.url_code:
            ran_str = ''.join(random.choices(self.pool, k=5))
            code = 'http://tiny_url.com' + ran_str
            self.code_url[code] = longUrl
            self.url_code[longUrl] = code
        return self.url_code[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code_url[shortUrl]