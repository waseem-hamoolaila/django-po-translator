from django import test
import os 

from django_po_translator.translate import translate_text
from django_po_translator.processors import lines_processor
import django_po_translator.app_settings as app_settings


class TestPoTranslator(test.TestCase):
                
     def test_translate_ep(self):

          translated_text = translate_text(text="Hello",target_language="ar")
          self.assertIsNotNone(translated_text)
          
          
     def test_lines_processor(self):
          lines = None
          po_test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'test_po.po'))
          with open(po_test_file_path, 'r', encoding='utf-8') as po_file:
               lines = po_file.readlines()
               
          self.assertIsNotNone(lines)