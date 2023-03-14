from django.test import TestCase


from .translate import translate_text


class TestPoTranslator(TestCase):
    
    def setUp(self):
        return super().setUp()
    
    
    def test_translation_ep(self):
        
        translated_text = translate_text(text="Hello",target_language="ar")
        self.assertIsNotNone(translated_text)        
        
    