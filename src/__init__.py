# Model credentials
URL = "https://www.google.com/search"
HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"" AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/84.0.4147.135 Safari/537.36",'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','DNT': '1','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1'}

# Import libraries
import requests
from bs4 import BeautifulSoup
import sys
import time
import json

def search(query):
    """ API calling for Feature snippet """
    time.sleep(3)
    SESSION = requests.Session()
    response = SESSION.get(URL, params={"q": query}, headers=HEADERS)
    document=BeautifulSoup(response.text, "html.parser")
    content = document.find_all("div", class_="kp-blk c2xzTb Wnoohf OJXvsb")
    display_text=content[0].find_all("div", class_="ifM9O")[0]
    if len(display_text.find_all("div", class_="mod"))==1:
        snippet=str(display_text.find_all("div", class_="mod")[0])
    else:
        snippet=str(display_text.find_all("div", class_="mod")[1])
    url=str(display_text.find_all("div", class_="yuRUbf")[0].find('a').get('href'))
    title=str(display_text.find_all("h3", class_="LC20lb DKV0Md")[0].findAll('span')[0].text)
    titleup=str(display_text.find_all("div", class_="TbwUpd NJjxre")[0].text)            
    return({"snippet":snippet,"titleup":titleup,"title":title,"url":url})

 