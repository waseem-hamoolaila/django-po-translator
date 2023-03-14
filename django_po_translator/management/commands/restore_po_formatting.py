from django.core.management.base import BaseCommand
from django.conf import settings
import os

import django_po_translator.app_settings as app_settings


class Command(BaseCommand):
    help = 'Restore a po file to its original format'

    def handle(self, *args, **options):
        # languages = options['language']
        locale_dir = os.path.join(settings.BASE_DIR, 'locale')
        
        languages = []
        
        for language in settings.LANGUAGES:
            if os.path.exists(os.path.join(os.getcwd(), 'locale', language[0], 'LC_MESSAGES', app_settings.PO_FILES_NAME)):
                languages.append(language[0])
        
        for language in languages:
            po_path = os.path.join(locale_dir, language, 'LC_MESSAGES', app_settings.PO_FILES_NAME)
            # save a backup
            po_backup_path = os.path.join(locale_dir, language, 'LC_MESSAGES', 'django.po.bak')
            po_clean_path = os.path.join(locale_dir, language, 'LC_MESSAGES', 'django.po.clean')

            os.system(f'cp {po_path} {po_backup_path}')
            os.system(f'msgattrib --no-obsolete --no-location -o {po_clean_path} {po_path}')
            os.system(f'cp {po_clean_path} {po_path}')