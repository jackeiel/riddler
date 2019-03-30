#riddlerPythonPull

import bs4
import requests
import re
import shelve

pythonLinks=[]
riddlerLinks=[]

for n in range(1,17):
    
    res=requests.get('https://fivethirtyeight.com/tag/the-riddler/page/%d/' %(n))
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    allLinks=soup.select('#main a')
    
    for q in range(len(allLinks)):
        if allLinks[q].get('href') in riddlerLinks:
            continue
        if 'features' in allLinks[q].get('href'):
            riddlerLinks.append(allLinks[q].get('href'))

    print(len(riddlerLinks))
    print('page %d complete' %(n))
                                
python=re.compile('python|Python')
with open('links.txt', 'w') as f:
    for i in range(len(riddlerLinks)):
        res=requests.get(riddlerLinks[i])
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text,'html.parser')
        text=soup.getText()
        mo=python.search(text)
        if mo==None:
            continue
        else:
            f.write(riddlerLinks[i] + '\n')
            # pythonLinks.append(riddlerLinks[i])

   
print(len(pythonLinks))
               
