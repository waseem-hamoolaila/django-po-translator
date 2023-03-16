import os
from django.conf import settings  


def get_po_files_path(lan):
    """ Return the path of given po language """
    return os.path.join(os.getcwd(), 'locale', lan, 'LC_MESSAGES', 'django.po')


def get_all_po_files_paths():
    
    paths = []
    
    for language in settings.LANGUAGES:
        if os.path.exists(get_po_files_path(language[0])):
            paths.append([get_po_files_path(language[0]), language[0]])
            
    return paths