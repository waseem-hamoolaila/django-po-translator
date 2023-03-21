from django import test
import os

from django_po_translator.po_processor import PoProcessor

class TestPoProcessor(test.TestCase):
    
    def setUp(self):
        
        self.po_test_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_files', 'test_po.po'))
    
    def test_read_po_file(self):
        
        po_processor = PoProcessor(po_file_path=self.po_test_file_path, target_language='ar')
        self.assertNotEqual(po_processor.get_po_files_entries(), [])
        
    def test_initial_resolve_fuzzy(self):
        
        po_processor = PoProcessor(po_file_path=self.po_test_file_path, target_language='ar')
        original_po_entries = po_processor.get_po_files_entries()
        
        self.assertTrue(po_processor.initial_resolve_fuzziness())
        self.assertNotIn("#, fuzzy\n", po_processor.get_po_files_entries())
        
        # restore original state    
        po_processor.update_po_dir(processed_entries=original_po_entries)
        
    
    def test_translate_po(self):
        
        po_processor = PoProcessor(po_file_path=self.po_test_file_path, target_language='ar')
        original_po_entries = po_processor.get_po_files_entries()
        
        self.assertTrue(po_processor.initial_translation_process(all=True))
        self.assertNotIn("msgstr ""\n", po_processor.get_po_files_entries())
        
        # restore original state    
        po_processor.update_po_dir(processed_entries=original_po_entries)