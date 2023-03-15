from django import test
import os 
from django.core.management import call_command
from django.core.management.base import CommandParser

from io import StringIO

from django_po_translator.management.commands.translate import BaseCommand as TranslateCommand

from django_po_translator.translate import translate_text
from django_po_translator.processors import lines_processor, action
import django_po_translator.app_settings as app_settings


class TestPoTranslator(test.TestCase):
                
     def test_translate_ep(self):

          translated_text = translate_text(text="Hello",target_language="ar")
          self.assertIsNotNone(translated_text)
          
          
     def test_action_processor(self):
          lines = None
          po_test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'test_po.po'))
          with open(po_test_file_path, 'r', encoding='utf-8') as po_file:
               lines = po_file.readlines()
               
          self.assertIsNotNone(lines)
          
          
     def test_line_processor(self):
          
          lines = None
          po_test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'test_po.po'))
          with open(po_test_file_path, 'r', encoding='utf-8') as po_file:
               lines = po_file.readlines()
               
          res, lines = lines_processor(lines, 'ar', update_already_translated=True, resolve_fuzzy=True)
          
          self.assertTrue(res)
          self.assertNotEqual(len(lines), 0)
          
          
     def test_line_processor_after_fixing_fuzziness(self):
          
          lines = None
          po_test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'test_po.po'))
          with open(po_test_file_path, 'r', encoding='utf-8') as po_file:
               lines = po_file.readlines()
          
          self.assertEqual(lines.count("#, fuzzy\n"), 2)
          res, lines = lines_processor(lines, 'ar', update_already_translated=True, resolve_fuzzy=True)
          
          self.assertTrue(res)
          self.assertNotEqual(len(lines), 0)
          self.assertEqual(lines.count("#, fuzzy\n"), 1) # only the one in the title
          
          
     def test_line_processor_without_fixing_fuzziness(self):
          
          lines = None
          po_test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'test_po.po'))
          with open(po_test_file_path, 'r', encoding='utf-8') as po_file:
               lines = po_file.readlines()
          
          self.assertEqual(lines.count("#, fuzzy\n"), 2)
          res, lines = lines_processor(lines, 'ar', update_already_translated=True, resolve_fuzzy=False)
          
          self.assertTrue(res)
          self.assertNotEqual(len(lines), 0)
          self.assertEqual(lines.count("#, fuzzy\n"), 2) # only the one in the title
          
          
     def test_line_processor_without_override_translations(self):
          
          lines = None
          po_test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'test_po.po'))
          with open(po_test_file_path, 'r', encoding='utf-8') as po_file:
               lines = po_file.readlines()
          
          # This is a wrong translation .. added intentionally
          self.assertEqual(lines.count('msgstr "صحيح"\n'), 1)
            
          res, lines = lines_processor(lines, 'ar', update_already_translated=False, resolve_fuzzy=True)
          
          # wrong translation should be stick in there .. without any change
          self.assertEqual(lines.count('msgstr "صحيح"\n'), 1)
        
     
     def test_line_processor_with_override_translations(self):
          
          lines = None
          po_test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'test_po.po'))
          with open(po_test_file_path, 'r', encoding='utf-8') as po_file:
               lines = po_file.readlines()
          
          # This is a wrong translation .. added intentionally
          self.assertEqual(lines.count('msgstr "صحيح"\n'), 1)
            
          res, lines = lines_processor(lines, 'ar', update_already_translated=True, resolve_fuzzy=True)
          
          # wrong translation should be overridden
          self.assertEqual(lines.count('msgstr "صحيح"\n'), 0)
     
     