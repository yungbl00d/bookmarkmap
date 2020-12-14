from bs4 import BeautifulSoup
import urllib.request

from bs4 import Comment

from mysite.memexplus.models import BasicBookmark


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

filename = "../../normallinks"

file = open(filename, 'r')
count = 0
for line in file.readlines():
    url = line.lstrip().split('"')[1]
    print(url)
    try:
        html = urllib.request.urlopen(url).read()
        print(text_from_html(html))
        b = BasicBookmark(
            full_text=text_from_html(html)
        )

    except:
        count += 1
        print(f'failed = {count}')
        pass
