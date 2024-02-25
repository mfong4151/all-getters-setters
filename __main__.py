from os import listdir
from arg_parser import parser
from utils.constants import JAVA_EXT
from procedure import main_procedure

if __name__ == "__main__":
    args = parser.parse_args()
    
    cwd_files = args.args if len(args.args) else listdir()
    
    files = [file for file in cwd_files if JAVA_EXT in file]

    for file in files:
        main_procedure(f"./{file}")                
