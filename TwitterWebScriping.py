from selenium import webdriver
from bs4 import BeautifulSoup as soup 
import time

driverpath = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
#hide google chrom
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
driver = webdriver.Chrome(driverpath,options=opt)

def TwitterPost(twitter_name):

    url = 'https://twitter.com/{}'.format(twitter_name)
    driver.get(url)
    time.sleep(5)

    # pixel = 0
    # for i in range(3):
    # 		driver.execute_script("window.scrollTo(0, {})".format(pixel))
    # 		time.sleep(3)
    # 		pixel = pixel + 10000
            

    page_html = driver.page_source  #print out html

    data = soup(page_html, 'html.parser')
    # print(data)
    # f = open("test2.html", "w",encoding='utf-8')
    # f.write(str(data))
    # f.close()

    posts = data.find_all('span',{'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
    # print(posts)

    founddot = False

    allpost = []
    for p in posts:
        txt = p.text
        if founddot == True:
            allpost.append(txt)
            # print(txt)
            # print('------------------')
            founddot = False

        if txt == '·':
            founddot = True

    

    return allpost
from songline import Sendline
token = '0MDrgIKGY9aET3Xxsy01cAfkY1hoxIoqfRgLpDj4GLR'
messenger = Sendline(token)
for i in range(100000):
    messenger.sendtext('รักเทอๆ')

checkTwitter = ['elonmusk','BillGates']
for ct in checkTwitter:
    texttoline = ''
    post = TwitterPost(ct)
    print("----- {} -----".format(ct))
    texttoline += '----- {} -----\n'.format(ct)
    for p in post:
        texttoline += p + '\n\n'
        print("==========")
    messenger.sendtext(texttoline)

driver.close()

