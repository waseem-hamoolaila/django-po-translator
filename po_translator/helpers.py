from .translate import translate_text


def process_lines(lines, lan, update_already_translated=False):
    """
    parse msgid and msgid and apply the translation to a new list
    
    return, processed list.
    """
    
    processed_lines = []
    
    for index, line in enumerate(lines):
    
        if is_message_str(line):
            # update even if the msgstr already provided
            if update_already_translated:
                msgid = get_msgid(lines, msgstr_index=index)
                translated_string = fetch_translation(string=msgid, lan=lan)
                processed_lines.append('msgstr "' + translated_string + '"\n' )
                
            else:
                msgstr = get_str(line)
                if msgstr == '':
                    msgid = get_msgid(lines, msgstr_index=index)
                    translated_string = fetch_translation(string=msgid, lan=lan)
                    processed_lines.append('msgstr "' + translated_string + '"\n' )
                    
                else:
                    processed_lines.append(line)
        else:
            processed_lines.append(line)
    
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
        print(lines[msgstr_index - 1].split('"')[1] )
        return lines[msgstr_index - 1].split('"')[1] if lines[msgstr_index - 1].split('"')[1] != '"' else None
    except:
        raise ValueError("Not valid msgstr index.")
    
    
def fetch_translation(string, lan):
    """ Translate the giving word """
    if string != "":
        # Translate some text
        result = translate_text(text=string, target_language=lan)
        return result if result else ''
    
    return ''




