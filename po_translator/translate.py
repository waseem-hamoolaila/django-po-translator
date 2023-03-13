import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import po_translator.app_settings as app_settings

def translate_text(text, target_language):
    
    base_url = app_settings.GOOGLE_TRANSLATOR_BASE_URL
    url = base_url + 'm?hl=en&sl=auto&tl=' + urllib.parse.quote(target_language) + '&ie=UTF-8&prev=_m&q=' + urllib.parse.quote(text)
    
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    
    translated_text = soup.find('div', {'class': app_settings.GOGGLE_RESULT_DIV_CONTAINER_CLASS}).text
    
    return translated_text