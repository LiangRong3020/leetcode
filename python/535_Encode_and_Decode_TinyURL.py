class Codec:

    def __init__(self):
        self.record_longurl = {}
        self.record_shorturl = {}
        self.url_count = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        now_url = 'http://tinyurl.com/' + str(self.url_count)
        self.url_count += 1
        self.record_longurl[longUrl] = now_url
        self.record_shorturl[now_url] = longUrl

        return now_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        return self.record_shorturl[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))