import os
from django.core.management import BaseCommand
from django_po_translator.helpers import get_all_po_files_paths, reformat_po_file, run_make_messages


from django_po_translator.po_processor import PoProcessor


class Command(BaseCommand):
    
    help = 'Translate Po files and fix fuzziness'
    
    def add_arguments(self, parser):
        parser.add_argument('--translate-existed', dest='translate-existed', action='store_true', 
                            help='Translate and update already existed translations, the current translation will be overridden')
        
        parser.add_argument('--resolve-fuzzy', dest='resolve-fuzzy', action='store_true', 
                            help='Remove all fuzziness by re-translating the msgid and remove #, fuzzy keyword')


    def handle(self, *args, **options):
        
        translate_existed = options.get('translate-existed', False)
        resolve_fuzzy = options.get('resolve-fuzzy', False)
        
        self.stdout.write("\n \n")
        self.stdout.write(self.style.SUCCESS("New Process has been initiated"))
        self.stdout.write("\n")
        
        if translate_existed:
            self.stdout.write("Translate exited ... ", ending=' ')
            self.stdout.write(self.style.SUCCESS("Yes"))
        else:
            self.stdout.write("Translate exited ... ", ending=' ')
            self.stdout.write(self.style.ERROR("No"))
            
        if resolve_fuzzy:
            self.stdout.write("Resolve fuzzy ... ", ending=' ')
            self.stdout.write(self.style.SUCCESS("Yes"))
            self.stdout.write("\n")
        else:
            self.stdout.write("Resolve fuzzy ... ", ending=' ')
            self.stdout.write(self.style.ERROR("No"))
            self.stdout.write("\n")
        
        
        result = reformat_po_file()
        self.stdout.write("Reformatting ...", ending=" ")
        
        if not result:
            self.stdout.write(self.style.ERROR("failed \n"))
            return
            
        self.stdout.write(self.style.SUCCESS("success \n"))
        
        
        result = run_make_messages()
        self.stdout.write("Make messages ...", ending=" ")
        
        if not result:
             self.stdout.write(self.style.ERROR("failed \n"))
             self.stdout.write(self.style.ERROR("Check the error mentioned in the log. \n"))
             return
        
        self.stdout.write(self.style.SUCCESS("success \n"))
        
        for path in get_all_po_files_paths():
           
            po_tool = PoProcessor(po_file_path=path[0], target_language=path[1])
            self.stdout.write(f"Processing {path[1]}: Total {po_tool.get_total_translation()} - Missing: {po_tool.get_number_of_missing_trans()}")
            
            if translate_existed:
                result = po_tool.initial_translation_process(all=True)
            else:
                result = po_tool.initial_translation_process()
                
            if resolve_fuzzy:
                result = po_tool.initial_resolve_fuzziness()
                        
            self.stdout.write(f"Finished processing {path[1]} file, the result is .....", ending=" ")
            if result:
                self.stdout.write(self.style.SUCCESS("success"))
            else: 
                self.stdout.write(self.style.ERROR("failed"))
            
            self.stdout.write("\n")
        
        self.stdout.write("processing is completed.")
        self.stdout.write("\n \n")