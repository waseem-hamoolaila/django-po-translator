import os
from django.core.management import BaseCommand
from django.conf import settings  
from helpers import get_po_files_path, get_all_po_files_paths

from django_po_translator.po_processor import PoProcessor

class Command(BaseCommand):
    
    help = 'Translate Po files and fix fuzziness'
    
    def add_arguments(self, parser):
        parser.add_argument('--translate-existed', dest='translate-existed', action='store_true', 
                            help='Translate and update already existed translations, the current translation will be overridden')
        
        parser.add_argument('--resolve-fuzzy', dest='resolve-fuzzy', action='store_true', 
                            help='Remove all fuzziness by re-translating the msgid and remove #, fuzzy keyword')


    def handle(self, *args, **options):
        
        translate_existed = options.get('translate-existed', False)
        resolve_fuzzy = options.get('resolve-fuzzy', False)
        
        self.stdout.write(self.style.SUCCESS("New Process has been initiated"))
        
        if translate_existed:
            self.stdout.write("Translate exited ... ", ending=' ')
            self.stdout.write(self.style.SUCCESS("Yes"))
        else:
            self.stdout.write("Translate exited ... ", ending=' ')
            self.stdout.write(self.style.Error("No"))
            
        if resolve_fuzzy:
            self.stdout.write("Resolve fuzzy ... ", ending=' ')
            self.stdout.write(self.style.SUCCESS("Yes"))
        else:
            self.stdout.write("Resolve fuzzy ... ", ending=' ')
            self.stdout.write(self.style.Error("No"))
            
        
        for path in get_all_po_files_paths():
           
            po_tool = PoProcessor(po_file_path=path[0], target_language=path[1])
            self.stdout.write(f"Processing {path[1]}: Total {po_tool.get_total_translation()} - Missing: {po_tool.get_number_of_missing_trans()}")
            
            po_tool.initial_translation_process(all=True)
            
            self.stdout.write(f"Finished processing {path[1]} file, the result is .....", ending=" ")
            self.stdout.write(self.style.SUCCESS("Success"))