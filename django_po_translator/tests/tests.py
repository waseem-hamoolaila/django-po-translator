import pytest

from django_po_translator.translate import translate_text
import django_po_translator.app_settings as app_settings

                
def test_translate_ep(client):

     translated_text = translate_text(text="Hello",target_language="ar")
     assert translate_text is not None        