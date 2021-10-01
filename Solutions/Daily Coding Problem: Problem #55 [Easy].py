# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Implement a URL shortener with the following methods:
#
#  * shorten(url), which shortens the url into a six-character alphanumeric
#    string, such as zLg6wl.
#  * restore(short), which expands the shortened string into the original url. If
#    no such shortened string exists, return null.
#
# Hint: What if we enter the same URL twice?
#
#
# --------------------------------------------------------------------------------
#
#
class URL_shortener():
    def __init__(self):
        super(URL_shortener, self).__init__()
        self.hash_table = {}
        self.map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def shorten(self, url):
        def get_id(string):
            num = ""
            for letter in url:
                s = str(ord(letter))
                s = s.rjust(3, "9")
                num += s
            id = int(num)
            return id

        id = get_id(url)
        short_url = ""
        while(id > 0):
            short_url += self.map[id % 62]
            id //= 62
        if len(short_url) < 6:
            while len(short_url) < 6:
                short_url = short_url + self.map[ord(short_url[-1]) % 62]
        else:
            short_url = short_url[:6]
        self.hash_table[short_url] = url
        return short_url

    def restore(self, short):
        return self.hash_table.get(short)


short = URL_shortener()
short_url = short.shorten("abc")
print(short_url)
restored_url = short.restore(short_url)
restored_url1 = short.restore("abcdfg")
print(restored_url)
print(restored_url1)
