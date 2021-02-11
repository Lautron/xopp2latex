import gzip, re, glob
from xml.dom import minidom

def get_files():
    files = glob.glob('*.xopp')
    return files 

def parse_file(filename):
    with gzip.open(filename, 'r') as filedata:
        xmldoc = minidom.parseString(filedata.read())
        itemlist = xmldoc.getElementsByTagName('teximage')
        result = [s.attributes['text'].value for s in itemlist]
        return result
        
def write_file(formulas):
    strings = ['$' + '$\n\n$'.join(arr) + '$' for arr in formulas]
    if not strings:
        print("Couldn't find any formulas to extract")
        return 

    with open('extracted_formulas.pmd', 'w') as fileobj:
        fileobj.write('\n\n\\rule{5in}{0.4pt}\n\n'.join(strings))
    print('Extracted formulas to "extracted_formulas.pmd"')

def main():
    files = get_files()
    formulas = [parse_file(filename) for filename in files]
    write_file(formulas)

if __name__ == '__main__':
    main()
