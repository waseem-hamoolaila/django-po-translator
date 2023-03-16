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

def reformat_po_file():
    
    for path in get_all_po_files_paths():
        po_path = os.path.join(os.getcwd(), 'locale', path[1], 'LC_MESSAGES', 'django.po')
        po_backup_path = os.path.join(os.getcwd(), 'locale', path[1], 'LC_MESSAGES', 'django.po.bak')
        po_clean_path = os.path.join(os.getcwd(), 'locale', path[1], 'LC_MESSAGES', 'django.po.clean')

        os.system(f'cp {po_path} {po_backup_path}')
        result = os.system(f'msgattrib --no-obsolete --no-location -o {po_clean_path} {po_path}')
        os.system(f'cp {po_clean_path} {po_path}')
        
        if result != 0:
            return False
        
    return True

def run_make_messages():
    
    result = os.system("python manage.py makemessages -a")
    
    if result == 0:
        return True
    return False
    