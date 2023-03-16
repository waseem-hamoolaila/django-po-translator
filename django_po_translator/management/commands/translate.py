import os
from django.core.management import BaseCommand
from django.conf import settings  

from django_po_translator.po_processor import PoTools
# from django_po_translator.processors import lines_processor, action

class Command(BaseCommand):
    
    help = 'Manage Django PO files.'
    # TODO: redo this section
    
    def add_arguments(self, parser):
        parser.add_argument('--translate-existed', dest='translate-existed', action='store_true', 
                            help='Translate and update already existed translations, the current translation will be overridden')
        
        parser.add_argument('--resolve-fuzzy', dest='resolve-fuzzy', action='store_true', 
                            help='Remove all fuzziness by re-translating the msgid and remove #, fuzzy keyword')


    def handle(self, *args, **options):
        
        translate_existed = options.get('translate-existed', False)
        resolve_fuzzy = options.get('resolve-fuzzy', False)
        
        # action(command=self, translate_existed=translate_existed, 
        #                     resolve_fuzzy=resolve_fuzzy)
        
        po_path = os.path.join(os.getcwd(), 'locale', 'ar', 'LC_MESSAGES', 'django.po')
        po_tool = PoTools(po_file_path=po_path, target_language='ar')
        
        po_tool.initial_translation_process(all=True)