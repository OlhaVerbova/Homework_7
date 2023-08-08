import re
def normalize(text: str)-> str:    
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}  
    
    mini_cy = tuple(CYRILLIC_SYMBOLS)
    for c, l in zip(mini_cy, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    temp_name = text.translate(TRANS)
    pat = r"[^\w\d]+"
    result_name = re.sub(pat, "_", temp_name)
    
    return result_name