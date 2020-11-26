import json
from bs4 import BeautifulSoup
import requests

url = 'http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
web = requests.get(url)

Out = BeautifulSoup(web.content, 'html.parser')

kosong = []
for i in Out.find_all('strong'):
    kosong.append(i.text.split())    # Pertama saya buat agar semua text pada element strong dimasukkan kedalam empty list
    
list_ultraman = [{'Ultraman' : {}}, {'Monster' : {}}] #Saya buat list kosong yang berisi nested dictionaries sesuai dengan format yang diminta

for ultraman in range(2,36): #Dikarenakan ultraman terdapat pada index 2 sampai 35 maka in range 2, 36
    kosong[ultraman] = [kosong[ultraman][0], ' '.join(kosong[ultraman][1:])] #kosong[2] = index 0 tetap, index berikutnya sampe akhir di gabung
    list_ultraman[0]['Ultraman'][kosong[ultraman][0]] = kosong[ultraman][1] #Berikut format untuk menambah key pada suatu key dalam nested dictionaries
    
for monster in range(37, 110):
    kosong[monster] = [kosong[monster][0], ' '.join(kosong[monster][1:])]
    list_ultraman[1]['Monster'][kosong[monster][0]] = kosong[monster][1]


# with open('Scrap.json', 'w') as file:
#     json.dump(list_ultraman, file)

print(list_ultraman)