import os
from django.core.management import BaseCommand
from django.conf import settings  

from po_translator.helpers import process_lines, action

class Command(BaseCommand):
    
    help = 'Manage Django PO files.'
    
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        res, cause = action(command=self)
        
        print(res, cause)
        