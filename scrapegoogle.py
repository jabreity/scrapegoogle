import sys
import requests
from bs4 import BeautifulSoup
import urllib3
text = sys.argv[1]
resultsval = int(sys.argv[2])
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
def search_google(text, max_results=100):
    ## split then join to convert spaces to + in link
    url = 'https://www.google.com/search?q=' + '+'.join(text.split()) + '&num=100'
    print('From', url, '\n---\n')
    headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15'
    }
    soup = BeautifulSoup(requests.get(url, headers=headers, verify=False).content, "html.parser")
    #print(soup) 
    ## loop through only the first results up to max_results

    #for i in soup.select('h3'):
    #    print(i.text)
    #    print(i.select('a'))
    #    print(soup.select('h3 a'))
    #    print(i.select('h4'))
    #print(soup.find_all("href", attrs={"class": "rcuQ6b"}))
    #for i in soup.find_all(['h3'])[:max_results]:
    #    print(i) 
    #    for d in i:
    #        print(d)
    #    
    #    print('\n---\n') ## separate results
    #iresults = []
    #for g in soup.find_all('div', {'class':'g'}):
    #    if anchors:
    #        link = anchors[0]['href']
    #        title = g.find('h3').text
    #        results.append(str(title))

    results = []
    for g in soup.find_all('div',  {'class':'g'})[:max_results]:
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            try:
                description_tag = g.find('div',{'class': 'VwiC3b'}).text
                #description = g.find('div', {'data-sncf':'2'}).text
            except Exception as e:
                description = "-"
            results.append(str(title)+"\n"+str(link)+'\n'+str(description_tag))

    for i in results:
        print(i+"\n")

search_google(text, resultsval)
