import os
from django.conf import settings
from django.core.management import BaseCommand
from .translate import translate_text

import po_translator.app_settings as app_settings

def process_lines(lines, lan, update_already_translated=False, resolve_fuzzy=False):
    """
    parse msgid and msgid and apply the translation to a new list
    
    return, processed list.
    """
    
    processed_lines = []
        
    for index, line in enumerate(lines):
    
        if is_message_str(line):
            # update even if the msgstr already provided
            if update_already_translated:
                processed_lines = translate_msgstr_line(processed_lines, lines, index, lan)    
            else:
                msgstr = get_str(line)
                if msgstr == '':
                    processed_lines = translate_msgstr_line(processed_lines, lines, index, lan)
                else:
                    # msgstr already provided ... keep it as it is
                    processed_lines.append(line)
        else:
            processed_lines.append(line)
    
    return processed_lines


def translate_msgstr_line(processed_lines:list, lines:list, index, lan):
    msgid = get_msgid(lines, msgstr_index=index)
    translated_text = fetch_translation(text=msgid, lan=lan)
    processed_lines.append('msgstr "' + translated_text + '"\n' )
    
    return processed_lines


def is_message_id(line) -> bool:
    """ 
    Return if the line is message id 
    
    return: bool
    """
    try:
        if line.split(" ")[0] == "msgid":
            return True
        return False
    except:
        return False


def is_message_str(line):
    """ 
    Return if the line is message str
    
    return: bool
    """
    try:
        if line.split(" ")[0] == "msgstr":
            return True
        return False
    except:
        return False
    

def get_str(line):
    """ Return the string is exist and None if the msgstr is empty """
    if is_message_str(line): # TODO remove if not necessary
        return line.split('"')[1] if line.split('"')[1] != '"' else None

def get_msgid(lines, msgstr_index):
    """ Return the msgid of a given msgstr index """
    try:
        return lines[msgstr_index - 1].split('"')[1] if lines[msgstr_index - 1].split('"')[1] != '"' else None
    except:
        raise ValueError("Not valid msgstr index.")
    
    
def fetch_translation(text, lan):
    """ Translate the giving word """
    if text != "":
        # Translate some text
        result = translate_text(text=text, target_language=lan)
        return result if result else ''
    
    return ''


def is_fuzzy(lines, msgstr_index):
    """ Determine whether this translation is fuzzy """
    try:
        return lines[msgstr_index - 2].split("\n")[0] == "#, fuzzy"
    except:
        return False


def action(command:BaseCommand, translate_existed, resolve_fuzzy):
    """ 
    Apply the actions into the PO files
    
    args 
    - command: the command that is calling this function
    
    return bool, string
    """
    
    languages = None
    try:
        languages = [language[0] for language in settings.LANGUAGES]
    except:
        return False, "No languages detect in the project, make sure LANGUAGES is defined in project settings"
    
    po_files_paths = []
    for language in languages: 
        if os.path.exists(os.path.join(os.getcwd(), 'locale', language, 'LC_MESSAGES', app_settings.PO_FILES_NAME)):
            po_file = os.path.join(os.getcwd(), 'locale', language, 'LC_MESSAGES', app_settings.PO_FILES_NAME)
            po_files_paths.append((po_file, language))
    
    if not po_files_paths:
        return False, "No po files detected in the project."
        
        
    # Update all the po files
    for po_file_details in po_files_paths:
        
        po_file_path = po_file_details[0]
        po_file_language = po_file_details[1]
        
        lines = None
        with open(po_file_path, 'r', encoding='utf-8') as po_file:
            lines = po_file.readlines()
                
        if lines:
            with open(po_file_path, 'w', encoding='utf-8') as po_file:
                processed_list = process_lines(lines=lines, lan=po_file_language, 
                                               update_already_translated=translate_existed, 
                                               resolve_fuzzy=resolve_fuzzy)
                for line in processed_list:
                    po_file.write(line)
        else:
            command.stdout.write(f"{po_file_language} Po file is empty .. no translations were added.")

        
    command.stdout.write(f"Completed ... {len(po_files_paths)} Po file/s have been processed")
    
    
    return True, "Done"