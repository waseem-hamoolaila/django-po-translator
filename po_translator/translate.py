import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

def translate_text(text, target_language):
    # Set up the Google Translate URL
    base_url = 'https://translate.google.com/'
    url = base_url + 'm?hl=en&sl=auto&tl=' + urllib.parse.quote(target_language) + '&ie=UTF-8&prev=_m&q=' + urllib.parse.quote(text)
    
    # Send a request to Google Translate and parse the response
    req = urllib.request.urlopen(url)
    soup = BeautifulSoup(req, 'html.parser')
    
    translated_text = soup.find('div', {'class': 'result-container'}).text
    
    return translated_text