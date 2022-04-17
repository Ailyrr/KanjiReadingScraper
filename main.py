from asyncore import read
from nturl2path import url2pathname
from click import pass_context
from requests_html import HTMLSession

def scrapeKanjis(char):
    url = f'https://jisho.org/search/{char}'
    session = HTMLSession()
    r = session.get(url)
    kunOnReadings = [] 
    readings = r.html.find('span.japanese_gothic')
    for r in readings:
        kunOnReadings.append(r.find('a', first= True).text.strip())
    kunOnReadings.pop(0)
    return kunOnReadings

def writeNewCardEntry(char, readings):
    txtFile = open('outText.txt', 'a')
    txtFile.write(char + "@")
    for e in readings:
        txtFile.write(e + ", ")
    txtFile.write('\n')
    txtFile.close()

def autoLookupAnkiMaster():
    document = open('sourceText.txt', 'r')
    lines = document.readlines()
    for kanji in lines:
        readingArray = scrapeKanjis(str(kanji[0]))
        print('Added: ' + str(readingArray))
        writeNewCardEntry(kanji[0], readingArray)

autoLookupAnkiMaster()