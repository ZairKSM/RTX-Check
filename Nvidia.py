from selenium import webdriver
from bs4 import BeautifulSoup
from time import *
import json
import os

pathChrome = os.path.abspath(__file__).replace("Nvidia.py",'chromedriver.exe')
print(pathChrome)
urls = [
    'https://shop.nvidia.com/fr-fr/geforce/store/?page=1&limit=9&locale=fr-fr&gpu=RTX%203080,RTX%203070,RTX%203060%20Ti&manufacturer=NVIDIA&gpu_filter=RTX%203090~0,RTX%203080~1,RTX%203070~1,RTX%203060%20Ti~1,RTX%203060~0,RTX%202080%20Ti~0,RTX%202080%20SUPER~0,RTX%202080~0,RTX%202070%20SUPER~0,RTX%202070~0,RTX%202060~0,GTX%201660%20Ti~0,GTX%201660%20SUPER~0,GTX%201660~0,GTX%201650%20Ti~0,GTX%201650%20SUPER~0,GTX%201650~0'
]

RTX_Code =[
    'NVGFT080',
    'NVGFT070',
    'NVGFT060T',
]

def CheckNvidia():
    RTX= []
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=options,executable_path=pathChrome)
    driver.get(urls[0])

    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"lxml")
    driver.quit()

    name =soup.findAll("h2" ,{"class":"name"})
    image = soup.findAll("img", {"class": "featured-img"})
    stock = soup.findAll("a", {"class": "featured-buy-link"})
    price = soup.findAll("div",{"class":"price"})
    for i in range(len(RTX_Code)):
        #x=soup.find("div", {"class": RTX_Code[i]}).text
        #jsopar=json.loads(x.replace("[","").replace("]",""))
        RTX.append([
            name[i].text.replace("\n","").strip(),
            image[i].get('src'),
            price[i].text.replace("\n",""),
            stock[i].text.replace("\n","").strip(),
            soup.find("div", {"class": RTX_Code[i]}).text.replace("\n","")

        ])

    return RTX

"""while True:
    try:
        RTX = CheckNvidia()
    except:
        print('Une erreur est survenue probablement une carte graphique qui est disponible')
    for i in range(len(RTX)):
        if RTX[i][3]!= 'RUPTURE DE STOCK' :
            print("WLLH YA DU STOCK")
    sleep(30)"""
