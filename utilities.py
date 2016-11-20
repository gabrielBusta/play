import sys
import codecs
import json


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


def load_json(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8') as infile:
        return json.load(infile)


def write_json(json_object, file_path):
    with codecs.open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(json_object, outfile)


def pretty_print_json(json_object):
    uprint(json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': ')))
