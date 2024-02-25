pub_class_reg = r'^public class\s+(\w+)'
class_dec_reg =   r'\s([A-Z][a-z]*)\s>',  # Pattern 2: A capital word surrounded by spaces and a pointy bracket on the right
cap_word_reg = r'\s*\b[A-Z][a-zA-Z]*\s+\w+;'# Pattern 3: Any capitalized word followed by a lowercase letter that has a semicolon on the right
get_reg = r'\bget\b'
set_reg = r'\bset\b'