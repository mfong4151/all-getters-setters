
def write_getter_setter(instance_vars_types):
    getters_setters = []
    
    for var_type, var_name in instance_vars_types:
        getters_setters.append(write_getter(var_type, var_name)) 
        getters_setters.append(write_setter(var_type, var_name))
        
    return getters_setters

def write_getter(var_type, var_name):
    line_1 = f"    public {var_type} get{var_name.capitalize()}() {{\n"
    line_2 = f"        return this.{var_name};\n"
    line_3 = "    }\n"
    
    return f"{line_1}{line_2}{line_3}"

def write_setter(var_type, var_name):
    line_1 = f"    public void set{var_name.capitalize()}({var_type} {var_name}) {{\n"
    line_2 = f"        this.{var_name} = {var_name};\n"
    line_3 = "    }\n"
    
    return f"{line_1}{line_2}{line_3}"
