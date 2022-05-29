import requests
from bs4 import BeautifulSoup

def scrape(url,filename):
    """Scrape URLs to generate previews."""
    headers = requests.utils.default_headers()
    '''
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    '''
    r = requests.get(url, headers)
    raw_html = r.content
    soup = BeautifulSoup(raw_html, 'html.parser')
    # print(soup.prettify())
    html = soup.prettify("utf-8")
    with open(filename, "wb") as file:
        file.write(html)
        file.close()
    


url1 = 'https://foresignal.com/es/'
file1 = "ForexSenial.html"
print( 'bajando: '+url1+" en "+file1)
scrape(url1,file1)

''' Requiere acceder como usuario
url2 = 'https://my.xm.com/es/member/signals/calendar'
file2 = "XMsignal.html"
print( 'bajando: '+url2+" en "+file2)
scrape(url2,file2)
'''