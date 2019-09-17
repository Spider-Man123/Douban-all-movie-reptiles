from selenium import webdriver
from selenium .webdriver .support .ui import WebDriverWait
from selenium .webdriver .common.by import By
import time
import re
from selenium.webdriver .support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree
import requests
import os,shutil
import urllib .request
from selenium.webdriver.chrome.options import Options
nn=0
url='https://movie.douban.com/tag/#/'
browser=webdriver .Chrome()
browser.get(url)
list=[]
a = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located(
    (By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/a[1]/p/span[1]')))
time.sleep(3)
for ll in range(0,100):
    time.sleep(5)
    b=re.findall('data-id="\d\d\d\d\d\d\d\d"',browser .page_source )
    c=re.findall('data-id="\d\d\d\d\d\d\d"',browser .page_source )
    r=re.findall('img data-v.*jpg"',browser.page_source )
    urls=b+c
    for u in urls[nn:nn+20]:
        try:
            urll=u.replace('data-id=','').replace('"','')
            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities["pageLoadStrategy"] = "none"
            urlll = 'https://movie.douban.com/subject/{}/'.format(urll)
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            browser2 = webdriver.Chrome(options=chrome_options)
            browser2 .get(urlll)
            time.sleep(5)
            try:
                name = browser2.find_element_by_xpath('//*[@id="content"]/h1/span[1]')
                neirong = browser2.find_element_by_xpath('//*[@id="info"]')
                jianjie = browser2.find_element_by_xpath('//*[@id="link-report"]/span[1]')
                pinglun1 = browser2.find_element_by_xpath('//*[@id="hot-comments"]/div[1]/div/p/span')
                pinglun2 = browser2.find_element_by_xpath('//*[@id="hot-comments"]/div[2]/div/p/span')
                pinglun3 = browser2.find_element_by_xpath('//*[@id="hot-comments"]/div[3]/div/p/span')
            except :
                print("出错")
            r = requests.get(urlll)
            r.encoding = 'utf-8'
            html = etree.HTML(r.text)
            tupian = html.xpath('//img/@src')
            urllib.request.urlretrieve(tupian[0],name.text+'.jpg')
            os.mkdir(name.text)
            with open('{}.txt'.format(name.text) , 'a', encoding='utf-8')as fp:
                fp.write("电影名：" + name.text + '\n')
                fp.write(neirong.text + '\n')
                fp.write("内容简介：" + jianjie.text + '\n')
                fp.write("评论：" + '\n')
                fp.write("1." + pinglun1.text + '\n')
                fp.write("2." + pinglun2.text + '\n')
                fp.write("3." + pinglun3.text + '\n' + '\n' + '\n')
            shutil .move(name.text+'.txt',name.text)
            shutil .move(name.text+'.jpg',name.text)
            browser2.close()
        except :
            print("")
    print("完成一页")
    try:
        try:
            try:
                try:
                    d= WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located(
                        (By.XPATH, '//*[@id="app"]/div/div[1]/a')))
                    d.click()
                    nn = nn + 20
                except:
                    d = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located(
                        (By.XPATH, '//*[@id="app"]/div/div[1]/a')))
                    d.click()
                    nn = nn + 20
            except :
                d = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/div[1]/a')))
                d.click()
                nn = nn + 20
        except :
            d = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/div[1]/a')))
            d.click()
            nn = nn + 20
    except:
        print("")
