import os
from django.core.management import BaseCommand
from django.conf import settings  

from po_translator.helpers import process_lines

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

        lines = None
        with open(po_file_path, 'r', encoding='utf-8') as po_file:
            lines = po_file.readlines()
                
        if lines:
            with open(po_file_path, 'w', encoding='utf-8') as po_file:
                
                print(process_lines(lines=lines))
                for line in lines:
                    po_file.write(line)
        else:
            self.stdout.write("Po file is empty .. no translations were added.")
                
        