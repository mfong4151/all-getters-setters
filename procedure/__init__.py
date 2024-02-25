from utils.file_io import read_files, write_files
from procedure.parse_content import parse_content_list
from procedure.write_constructor import write_constructor
from procedure.write_getter_setter import write_getter_setter
from utils.colorize import colorize, RED, BOLD, DEFAULT, LIME_GREEN
# from listify_contents import listify_contents

def main_procedure(file):
    file_content=  read_files(file)
    parsed_file = parse_content_list(file_content)
    
    
    if all([not condition for condition in parsed_file]):
        print(colorize(RED, f"It seems that the file {BOLD}{file}{DEFAULT}{RED} has already populated getters and setters.\nIf you've edited your file, please rely on snippets to finish.\n"))
        return
        
    file_contents, class_declaration, instance_vars_types = parsed_file
    constructor = write_constructor(class_declaration, instance_vars_types)
    getters_setters = write_getter_setter(instance_vars_types)
    file_contents.extend([constructor, *getters_setters, "}"])
    new_file_contents = "\n".join(file_contents)
        
    write_files(file, new_file_contents)
    print(colorize(f"{BOLD}{LIME_GREEN}", f"Succesfully edited defaults for {file}\n"))
   
    return
