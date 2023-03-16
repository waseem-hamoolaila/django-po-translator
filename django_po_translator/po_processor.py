
from django_po_translator.translate import translate_text


class PoProcessor:
    """ 
    Collection of tools could be used in order to process PO files
    """
    
    def __init__(self, po_file_path, target_language):      
        self.po_file_path = po_file_path
        self.target_language = target_language
    
    
    def get_po_files_entries(self):
        """ 
        Extract the content of the PO file as a list
        """
        with open(self.po_file_path, 'r', encoding='utf-8') as po_file:
            return po_file.readlines()
        
    def is_msgid(self, po_line) -> bool:
        """ 
        Checks if the given line is msgid
        """
        try:
            if po_line.split(" ")[0] == "msgid":
                return True
            return False
        except:
            return False

    def is_msgstr(self, po_line):
        """ 
        Checks is the given line is msgstr
        """
        try:
            if po_line.split(" ")[0] == "msgstr":
                return True
            return False
        except:
            return False
    
    def get_text_from_msgid(self, msgid):
        """ Extract the text from msgid line """
        return msgid.split('"')[1] if msgid.split('"')[1] != '"' else ""
    
    def get_msgid(self, processed_entries, msgstr_index):
        """ Extract msgid from po line """
        return processed_entries[msgstr_index - 1]
    
    def translate(self, text):
        return translate_text(text=text, target_language=self.target_language)

    def reform_msgstr(self, translated_text):
        """ Reform msgid to PO format """
        return 'msgstr "' + translated_text + '"\n'

    def is_fuzzy_line(self, processed_entries, msgstr_index):
        """ Checks if the given Po msgstr is fuzzy """
        return processed_entries[msgstr_index - 2] == "#, fuzzy\n"

    def is_missing_translation(self, po_line):
        """ Checks if the given po line is not translated """
        return po_line.split('"')[1] == ""
    
    def get_number_of_missing_trans(self):
        
        processed_entries = self.get_po_files_entries()
        number = 0
        
        for entry in processed_entries:
            if self.is_msgstr(entry) and self.is_missing_translation(entry):
                number += 1
                
        return number - 1

    def get_total_translation(self):
        
        processed_entries = self.get_po_files_entries()
        number = 0
        
        for entry in processed_entries:
            if self.is_msgstr(entry):
                number += 1
                
        return number - 1
    
    def clear_fuzziness(self):
        """ Translate Only fuzzy words and resolve it """
        entries = self.get_po_files_entries()
        processed_entries = []
        fuzzy_indexes = []
        
        if not entries:
            return False, "This file is empty"
        

        for index, line in enumerate(entries):
            if self.is_msgstr(line) and self.is_fuzzy_line(processed_entries=processed_entries, msgstr_index=index):
                msgid = self.get_msgid(processed_entries=processed_entries, msgstr_index=index)
                text = self.get_text_from_msgid(msgid=msgid)
                translated_text = self.translate(text=text)
                processed_entries.append(self.reform_msgstr(translated_text))
                fuzzy_indexes.append(index - 2)
            else:
                processed_entries.append(line)
        
        processed_entries = [i for j, i in enumerate(processed_entries) if j not in fuzzy_indexes]
        
        return True, processed_entries
    
    def translate_missing(self):
        """ Translate only records with missing translations """
        entries = self.get_po_files_entries()
        processed_entries = []
        
        if not entries:
            return False, "This file is empty"
        
        for index, line in enumerate(entries):
            if self.is_msgstr(line) and self.is_missing_translation(line):
                msgid = self.get_msgid(processed_entries=processed_entries, msgstr_index=index)
                text = self.get_text_from_msgid(msgid=msgid)
                translated_text = self.translate(text=text)
                processed_entries.append(self.reform_msgstr(translated_text))
            else:
                processed_entries.append(line)
        
        return True, processed_entries
    
    def translate_all(self):
        """ Translation all records without resolving fuzziness """
        entries = self.get_po_files_entries()
        processed_entries = []
        
        if not entries:
            return False, "This file is empty"
        
        for index, line in enumerate(entries):
            if self.is_msgstr(line):
                msgid = self.get_msgid(processed_entries=processed_entries, msgstr_index=index)
                text = self.get_text_from_msgid(msgid=msgid)
                translated_text = self.translate(text=text)
                processed_entries.append(self.reform_msgstr(translated_text))
            else:
                processed_entries.append(line)
                        
        return True, processed_entries
    
    def update_po_dir(self, processed_entries):
        """ Update the correspondent PO file """
        with open(self.po_file_path, 'w', encoding='utf-8') as po_file:  
             for processed_line in processed_entries:
                po_file.write(processed_line)
    
  
    def initial_resolve_fuzziness(self):
        """ Initial resolving fuzziness process """
        result, processed_entries = self.clear_fuzziness()
        self.update_po_dir(processed_entries=processed_entries)
        
        return result
        
    def initial_translation_process(self, all=False):
        """ 
        Initial translation process
        
        ** all: determine process type
        
        """
        if all:
            result, processed_entries = self.translate_all()
            self.update_po_dir(processed_entries=processed_entries)
            
            return result
        
        result, processed_entries = self.translate_missing()
        self.update_po_dir(processed_entries=processed_entries)
                
        return result
    
        