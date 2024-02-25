# /home/mfong415/Advanced Scripting/all-gs/procedure/write_constructor.py

def write_constructor(class_name, instance_vars_types):
    
    constructor = []
    constructor.extend([
        
        f"    public {class_name}(",
        ", ".join([f"{var_type} {var_name}" for var_type, var_name in instance_vars_types]),
        ") {\n"
        
    ])
    
    for var_type, var_name in instance_vars_types:
        constructor.append( f"        this.{var_name} = {var_name};\n")
    constructor.append( "    }\n")
    return "".join(constructor)
