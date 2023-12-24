import os

def verify_search(text):
    search = ''
    if hasattr(text,"__len__") and len(text) > 1:
        for char in text:
            search += char+'+'
        return 'https://www.google.com/search?q='+search
    else:
        if 'www.' in text[0] or '.com' in text[0] and not ' ' in text[0]:
            if 'http://' in text[0]:
                return text[0].replace('http://','')
            else:
                return text[0]
        return 'https://www.google.com/search?q='+text[0]

def exec_search(search):
    if search != None:
        return os.system(f"start firefox {search}")
    else:
        return 'the search cannot be empty'
