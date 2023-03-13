import os
from django.core.management import BaseCommand
from django.conf import settings  

class Command(BaseCommand):
    
    help = 'Translate all PO files used in the project'
    
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        
        languages = None
        try:
            languages = [language[0] for language in settings.LANGUAGES]
        except:
            self.stdout.write("Please make sure that LANGUAGE is defined in the settings as a tuple")
        
        po_file_path = os.path.join(os.getcwd(), 'locale', 'ar', 'LC_MESSAGES', 'django.po')

        with open(po_file_path, 'r', encoding='utf-8') as po_file:
            for line in po_file:
                self.stdout.write(line.rstrip())