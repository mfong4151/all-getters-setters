from procedure.regex_matches import pub_class_reg, cap_word_reg, get_reg, set_reg
import re

## Use regex matching to get the class name 
## Use regex matching to get the attributes

MIN_LINE_LENGTH = 10

def parse_content_list(file_content):
    
    file_contents = file_content.split("\n")   
    class_declaration = ""
    instance_vars_types = []
    num_getters, num_setters = 0, 0
    
    for i, line in enumerate(file_contents):
        
        # Parse the class name
        if not class_declaration and re.match(pub_class_reg, line):
            class_declaration = line.split(" ")[2] 
        
        
        #Parse instance variable declarations 
        if class_declaration and re.match(cap_word_reg, line): 
            type, dec  = line.strip().rstrip(";").split(" ")
            instance_vars_types.append([type, dec])
        
        ##Optimized version to make sure we don't rewrite getters and setters
        if len(line) > MIN_LINE_LENGTH:

            if "get" in line:
                num_getters += 1
            
            if "set" in line: 
                num_setters += 1        
        
    ## Guard clause in case there are no getters or setters    
    if num_getters == num_setters and num_getters == len(instance_vars_types):
        return [], "", []    
    
    for i in range(len(file_contents) -1, -1, -1):
        maybe_semi = file_contents[i]
        file_contents.pop()
        
        if maybe_semi == "}":
            break    
    
    return file_contents, class_declaration, instance_vars_types

