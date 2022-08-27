import json

try:
    config = json.load(open('config.json', encoding='utf-8'))
except:
    config = {
        "charset": "abcdefghijklmnopqrstuvwxyz"
    }
    json.dump(config, open('config.json', 'w', encoding='utf-8'), indent=4)

charset = ''.join(sorted(list(set(' ' + config['charset']))))
