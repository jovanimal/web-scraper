import requests
import bs4 
import re

res = requests.get('https://www.malaysiastock.biz/Market-Watch.aspx')
stats = requests.get('https://www.malaysiastock.biz/Market-Gauge.aspx')

res_soup = bs4.BeautifulSoup(res.text, 'lxml')
stats_soup = bs4.BeautifulSoup(stats.text, 'lxml')

class Statistic:
    def __init__(self, klci, gainer, loser, unchanged, date):
        self.date = date
        self.klci = klci
        self.gainer = gainer
        self.loser = loser
        self.unchanged = unchanged

    def display(self):
        print(date + "\n" 
              "KLCI:",klci + "\n"
              "Gainer:", gainer + "\n"
              "Loser:", loser + "\n"
              "Unchanged:", unchanged)

klci = res_soup.find(id="MainContent_UC_KLCI_lbQuoteLast").getText()
gainer = stats_soup.find(id="lbGainerNo").getText()
loser = stats_soup.find(id="lbLosersNo").getText() 
unchanged = stats_soup.find(id="lbUnchangedNo").getText()
date = res_soup.find(style=re.compile("float:right")).getText()

today = Statistic(date, klci, gainer, loser, unchanged)
today.display()

# print(date)