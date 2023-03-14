import os
from django.core.management import BaseCommand
from django.conf import settings  

from po_translator.helpers import process_lines, action

class Command(BaseCommand):
    
    help = 'Manage Django PO files.'
    
    def add_arguments(self, parser):
        parser.add_argument('--translate-existed', dest='translate-existed', action='store_true', 
                            help='Translate and update already existed translations, the current translation will be overridden')


    def handle(self, *args, **options):
        
        translate_existed = options.get('translate-existed', False)
        
        res, cause = action(command=self, translate_existed=translate_existed)
        
        print(res, cause)
        