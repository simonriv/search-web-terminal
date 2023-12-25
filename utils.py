import os
import json

BROWSERS = {'chrome':'chrome','firefox':'firefox','edge':'msedge','explorer':'iexplore','opera':'opera','brave':'brave-browser'}
ENGINE = {'google':'https://www.google.com/search?q=','yahoo':'https://sg.search.yahoo.com/search?p=','bing':'https://www.bing.com/search?q=','duckduckgo':'https://duckduckgo.com/?q='}

def create_folder(path):
    try:
        os.mkdir(path)
        return True
    except FileExistsError:
        return False

def verify_config(config):
    if config['browser'].lower() in BROWSERS and config['engine'].lower().replace(' ','') in ENGINE:
        return True
    else:
        return False

def set_config(data):
    folder = create_folder('./config')

    if folder != None and verify_config(data):
        with open('config/config.json','w') as f:
            json.dump(data, f)
    else:
        return False

def read_config():
    folder = create_folder('./config')

    if folder != None:
        if not os.path.isfile('config/config.json'):
            with open('config/config.json', 'w') as f:
                json.dump({'browser':'firefox','engine':'google'},f)
        with open('config/config.json', 'r') as f:
            data = json.load(f)
        return data

def verify_tld(url):
    split_url = url.split('.')
    tld_extracted = '.'.join(split_url[:-1])
    if tld_extracted != '' and len(split_url) > 1 and not ' ' in url:
        return True
    else:
        return False

def verify_search(text):
    search = ''
    config = read_config()
    if hasattr(text,"__len__") and len(text) > 1:
        for char in text:
            search += char+'+'
        return ENGINE[config['engine']]+search
    else:
        if 'www.' in text[0] or verify_tld(text[0]):
            if 'http://' in text[0]:
                return text[0].replace('http://','')
            else:
                return text[0]
        return ENGINE[config['engine']]+text[0]

def exec_search(search):
    if search != None:
        config = read_config()
        return os.system(f"start {BROWSERS[config['browser']]} {search}")
    else:
        return 'the search cannot be empty'
