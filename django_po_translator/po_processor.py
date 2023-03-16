
from django_po_translator.translate import translate_text


class PoTools:
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
    
    
    def is_msgid(po_line) -> bool:
        """ 
        Checks if the given line is msgid
        """
        try:
            if po_line.split(" ")[0] == "msgid":
                return True
            return False
        except:
            return False


    def is_msgstr(po_line):
        """ 
        Checks is the given line is msgstr
        """
        try:
            if po_line.split(" ")[0] == "msgstr":
                return True
            return False
        except:
            return False
    
    def translate(self, text):
    
        return translate_text(text=text, target_language=self.target_language)


    def reform_msgstr(self, translated_text):
        return 'msgstr "' + translated_text + '"\n'
    
    def get_msgid(self, processed_entries, msgstr_index):
        return processed_entries[msgstr_index - 1]

    def clear_fuzziness(self):
        
        entries = self.get_po_files_entries().split("\n")
        processed_entries = []
        
        if not entries:
            return False, "This file is empty"
        

        for index, line in enumerate(entries):
            if self.is_msgstr(line):
                # update even if the msgstr already provided
                msgid = self.get_msgid(processed_entries=processed_entries, msgstr_index=index)
                translated_text = self.translate(msgid)
                processed_entries.append(self.reform_msgstr(translated_text))
                
            else:
                processed_entries.append(line)
        
        return processed_entries
    
    
    
    def update_po_dir(self, processed_entries):
        with open(self.po_file_path, 'w', encoding='utf-8') as po_file:  
             for processed_line in processed_entries:
                po_file.write(processed_line) 
                
        
    