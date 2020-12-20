from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import requests

# 關閉通知
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'notifications': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars") 

# 打啟動selenium 務必確認driver 檔案跟python 檔案要在同個資料夾中
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")

#輸入email  
context = driver.find_element_by_css_selector('#email')
context.send_keys('qlixilp@yahoo.com.tw') 

#輸入password 不要記我密碼
context = driver.find_element_by_css_selector('#pass')
context.send_keys('Kevin3466')

commit = driver.find_element_by_css_selector('button[type=''submit'']').click()
time.sleep(3)
spec_url = "https://www.facebook.com/groups/NTU.Head"
driver.get(spec_url)

for x in range(10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3) #如果跑不出來，可以把裡面的數字調大一點
    
# 用不到了
# k = len(driver.find_elements_by_xpath('//div/div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]'))
# for i in range(k):
#     ha = driver.find_element_by_xpath('//div/div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]')
#     try :
#         driver.execute_script('arguments[0].click();',ha)
#     except:
#         pass
#     time.sleep(0.5)


soup = BeautifulSoup(driver.page_source, 'lxml')
links2 = soup.find_all('a')
dictionary = {}
for i in links2:
    e = 'https://www.facebook.com/groups/NTU.Head/permalink'
    a =  i.get('href') 
    if e not in a:
        pass
    else:
        time.sleep(2) #如果跑不出來，可以把裡面的數字調大一點
        string = a.strip("https://www.facebook.com/groups/NTU.Head/permalink/")
        li = string.split('/')
        
        if li[0] not in dictionary:
            dictionary[li[0]] = 0
            driver.get(a)
            time.sleep(2) #如果跑不出來，可以把裡面的數字調大一點
            soup1 = BeautifulSoup(driver.page_source, 'lxml')
            titles1 = soup1.find(class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa fgxwclzu a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m")
            #如果是Windows的話,titles1 = soup1.find(class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m")
            titles2 = soup1.find(class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa fgxwclzu a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id")
            #如果是Windows的話,titles2 = soup1.find(class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id")
            try:
                print(titles1.text)
                print(a)
            except:
                print(titles2.text)
                print(a)