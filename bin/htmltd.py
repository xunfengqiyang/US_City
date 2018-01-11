import urllib
import urllib2
from bs4 import BeautifulSoup
from Tv import *
import json

class DMAByBS4():
    def __init__(self):
        self.tv = Tv()

        ''''' 
        Constructor 
        '''

    def get(self, url, coding):
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        htmls= response.read()
        htm = htmls.decode(coding, 'ignore')
        return htm


if  __name__ =="__main__":
    get = DMAByBS4()
    html = get.get("https://en.wikipedia.org/wiki/List_of_United_States_television_markets", "utf-8")
    soup=BeautifulSoup(html,"html.parser")
    # trs=soup.find_all(name='tr', attrs={'class':"tr"})
    trs = soup.find_all(["tr"])
    tvList = list()
    for tr in trs:
        tv = Tv()
        _soup = BeautifulSoup(str(tr) , "html.parser")
        tds = _soup.find_all(name='td')
        try:
            # tv.setRank(str(tds[0].string))
            # tv.setMarket(str(tds[1].string))
            # tv.setState(str(tds[2].string))
            # tv.setCounties(str(tds[3].string))
            # tv.setHouseholds(str(tds[4].string))
            # tv.setABC(str(tds[5].string))
            # tv.setCBS(str(tds[6].string))
            # tv.setFox(str(tds[7].string))
            # tv.setNBC(str(tds[8].string))
            # tv.setOther(str(tds[9].string))

            state = str(tds[1].string)
            households = str(tds[3].string)
            arr = households.split('(')
            value = arr[0].replace(',', '')
            dic = {
                'value': value,
                'name': state
            }

            tvList.append(dic)
        except:
            continue

    f = open('./export/tvList.json', 'w')
    f.write(json.dumps(tvList, ensure_ascii=False, indent=4))
    f.close()
