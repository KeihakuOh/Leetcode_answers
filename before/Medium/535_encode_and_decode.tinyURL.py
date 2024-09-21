import hashlib

class Codec:
    def __init__(self):
        self.urls = {}

    def hash_to(self, s):
        return 'https://tinyurl/' + hashlib.md5(s.encode()).hexdigest()

    def encode(self, long_url: str) -> str:  
        hash_key = self.hash_to(long_url)
        self.urls[hash_key] = long_url
        return hash_key
        
    def decode(self, short_url: str) -> str: 
        return self.urls[short_url]