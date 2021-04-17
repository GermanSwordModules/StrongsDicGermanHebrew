from mwclient import Site
import configparser
import sys
from bs4 import BeautifulSoup
import re

try:
	path = sys.argv[1]
except:
	print ("No path to import.cfg provided. Exiting.")

config = configparser.ConfigParser()
config.read(path+'/import.cfg')

site = config['SERVER']['site'].strip()
pathv = config['SERVER']['path'].strip()
login = config['SERVER'].getboolean('login')
name = config['SERVER']['name'].strip()
pw = config['SERVER']['pw'].strip()
filename = config['PATH']['filename'].strip()

# Connecting to Wiki
site = Site(site,path=pathv)
if login:
	site.login(name,pw)

# Read XML file
with open(filename) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# Read all entries and get the value from wiki
i = 1
references = {}
for entry in soup.find_all('entryfree'):
    i = i + 1
    #if i > 13:
    #    break
    number = entry['n'].split("|")[0]
    lemma = entry['n'].split("|")[1]
    print ("== "+number+" ===")
    page = site.pages[number]
    if page.text() != "":
        lemma = ""
        textn = ""
        if "#REDIRECT" in page.text():
            red = re.findall ("\\[\\[(.*?)\\]\\]",page.text().split("\n")[0])
            text = site.pages[red].text()
            found = False
            for line in text.split("\n"):
                if "= " in line and "Hebräisch" in line:
                    lemma = line.replace("=","").split(":")[1].strip()
                    found = True
                elif "= " in line:
                    found = False
                elif "[[Kategorie" in line:
                    continue
                elif "<references" in line:
                    continue
                elif found:
                    line = re.sub("\\[\\[(.*?)\\]\\]", r'<ref target="Strong:"\g<1>">\g<1></ref>', line)
                    line = re.sub("''(.*?)''", r'<hi rend="italic">\g<1></hi>', line)
                    textn = textn + line + "\n"
        else:
            text = page.text()
            for line in text.split("\n"):
                if "==" in line:
                    lemma = line.replace("==","").strip()
                elif "[[Kategorie" in line:
                    continue
                elif "<references" in line:
                    continue
                else:
                    line = re.sub("\\[\\[(.*?)\\]\\]", r'<ref target="Strong:\g<1>">\g<1></ref>', line)
                    line = re.sub("''(.*?)''", r'<hi rend="italic">\g<1></hi>', line)
                    textn = textn + line + "\n"
        textn = textn.replace("\n\n", "<lb/>\n\n")
        refs = re.findall (r"<ref>(.*?)</ref>", textn)
        for r in refs:
            if r in references:
                textn = textn.replace("<ref>"+r+"</ref>", " "+references[r])
            else:
                references[r] = "["+str(len(refs))+"]"
                textn = textn.replace("<ref>"+r+"</ref>", " "+references[r])
        #print (lemma)
        #print (textn)
        o = entry.find ("orth")
        o.string = lemma
        t = entry.find ("def")
        t.string = textn
# Fix the tags...
st = str(soup).replace("&lt;","<").replace("&gt;",">").replace("entryfree", "entryFree")
with open(filename, "w") as file:
    file.write(str(st))
for key, value in references.items():
	print (value + " "+key)
