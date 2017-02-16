import bs4, json, requests

class RSS_Item:
    def __init__(self, soup_tag):
        self.link = soup_tag.link.text
        self.title = soup_tag.title.text
        self.pub_date = soup_tag.pubDate.text

    def to_json(self):
        return json.dumps(self.__dict__)


test_url = "https://globenewswire.com/Rss/industry/1771/Coal"

response = requests.get(test_url)
# We start by making an HTTP request and storing the response as a Response object. 
# type(response): <class 'requests.models.Response'>
# The Response class has useful methods and properties, like the following...
content = response.text 
# This creates a string with the relevant RSS content. Now we just need to find the
# specific text content we care about. BUT parsing string content is a nightmare. Let's 
# stand on the shoulders of giants by using another third-party library.
soup = bs4.BeautifulSoup(content, "xml")
# Now we're dealing with a BeautifulSoup object, with tons of useful methods.
# type(soup): <class 'bs4.BeautifulSoup'>
# You can read more at https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# but the most useful method is find_all()...
soup_tags = soup.find_all("item")
# This creates a list of BeautifulSoup tag objects, with their own set of useful methods,
# and also filters out all the unimportant text content from the original HTTP response.
# type(soup_tags): <class 'bs4.element.ResultSet'>
# type(soup_tags[1]): <class 'bs4.element.Tag'>
# Unfortunately third-party libraries can only help SO MUCH. It's time to convert these
# tag objects into a more useful form, such as the RSS_Item class I defined above.
rss_items = [RSS_Item(soup_tag) for soup_tag in soup_tags]

