from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import requests
import jieba
import jieba.analyse
import operator
from operator import itemgetter, attrgetter

subscription = int(
    input('抽獎：1；遺失：2；實習：3；便當：4；討論：5；腳踏車：6；學生證：7；活動:8；團購：9；家教：10；宿舍:11；其他：12'))
# 我們要的分類
posts = []
drawing = []
find = []
internship = []
eat = []
discuss = []
bike = []
S_card = []
activity = []
shop = []
tutor = []
dorm = []
others = []
categories = [drawing, find, internship, eat, discuss,
              bike, S_card, activity, shop, tutor, dorm, others]
we_want_analyse_0 = posts  # 我們想要分類的文章，先裝在list 裡
we_want_analyse = [[0 for i in range(2)]for j in range(
    len(we_want_analyse_0))]  # 要將文章跟網址分開


# '/Users/yangchinwei/documents/GitHub/our-python-project/posts.txt'
facebook_account = input('Your Facebook Account:')  # 臉書帳號
facebook_password = input('Your Facebook Password:')  # 臉書密碼

# 關閉通知
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'notifications': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

# 打啟動selenium 務必確認driver 檔案跟python 檔案要在同個資料夾中
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")

# 輸入email
context = driver.find_element_by_css_selector('#email')
context.send_keys(facebook_account)

# 輸入password 
context = driver.find_element_by_css_selector('#pass')
context.send_keys(facebook_password)

commit = driver.find_element_by_css_selector('button[type=''submit'']').click()
time.sleep(3)
spec_url = "https://www.facebook.com/groups/NTU.Head?sorting_setting=CHRONOLOGICAL"
driver.get(spec_url)

for x in range(2):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)


soup = BeautifulSoup(driver.page_source, 'lxml')
links2 = soup.find_all('a')
dictionary = {}
for i in links2:
    url_filter= 'https://www.facebook.com/groups/NTU.Head/permalink'
    url = i.get('href')
    if url_filter not in url:
        pass
    else:
        time.sleep(2)
        string = url.strip(
            "https://www.facebook.com/groups/NTU.Head/permalink/")
        li = string.split('/')
        if li[0] not in dictionary:
            dictionary[li[0]] = 0
            driver.get(url)
            time.sleep(2)
            soup1 = BeautifulSoup(driver.page_source, 'lxml')
            # windows用註解的
            # titles1 = soup1.find(class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m')
            # titles2 = soup2.find(class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id')
            titles1 = soup1.find(
                class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa fgxwclzu a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m")
            titles2 = soup1.find(
                class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa fgxwclzu a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id")
            try:
                posts.append(titles1.text+url)

            except:
                posts.append(titles2.text+url)

we_want_analyse_0 = posts  # 我們想要分類的文章，先裝在list 裡
we_want_analyse = [[0 for i in range(2)]for j in range(
    len(we_want_analyse_0))]  # 要將文章跟網址分開

for i in range(len(we_want_analyse_0)):
    site = we_want_analyse_0[i].rfind('http')
    site_1 = we_want_analyse_0[i].rfind('[0]')
    wao_zu = we_want_analyse_0[i][site:]
    wen = we_want_analyse_0[i][:site]
    if we_want_analyse_0[i].count('[0]') != 0:
        wao_zu = we_want_analyse_0[i][site:site_1]

    we_want_analyse[i][0] = wen
    we_want_analyse[i][1] = wao_zu
for r in range(len(we_want_analyse)):
    # 結巴斷詞
    jieba.set_dictionary("dict.txt")
    type_word = 0
    words_2 = jieba.cut(we_want_analyse[r][0], cut_all=False)
    the_one = []
    for k in words_2:
        the_one.append(k)
    # 莊每一次斷詞後的結果

    if "抽獎" in the_one or "抽" in the_one or "抽出" in the_one:
        drawing.append(we_want_analyse[r])

    elif "遺失" in the_one or "撿" in the_one or "拾獲" in the_one or "協尋" in the_one or "掉" in the_one or "失主" in the_one or "失物" in the_one or "失物招領" in the_one:
        if "學生證" in the_one:
            S_card.append(we_want_analyse[r])
        else:
            find.append(we_want_analyse[r])
    elif "便當" in the_one:

        eat.append(we_want_analyse[r])
    elif "團購" in the_one:

        shop.append(we_want_analyse[r])
    elif "週" in the_one or "講座" in the_one or "社" in the_one or "之夜" in the_one:
        activity.append(we_want_analyse[r])
    elif "討論" in the_one or "請益" in the_one:

        discuss.append(we_want_analyse[r])
    elif "實習" in the_one:
        internship.append(we_want_analyse[r])

    elif "家教" in the_one:
        tutor.append(we_want_analyse[r])
    elif "腳踏車" in the_one:
        bike.append(we_want_analyse[r])
    elif "宿舍" in the_one:
        dorm.append(we_want_analyse[r])
    else:
        others.append(we_want_analyse[r])


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=payload)
    return r.status_code


token = '5QPJXzcaZuXgNzfY4CG2t7E20VNB2AWjBaZgb4NJhhk'  # 權杖
addr = str()
addr1 = str()
if len(categories[subscription-1]) > 0:
    if len(categories[subscription-1]) <= 8:
        for i in range(len(categories[subscription-1])):
            addr += categories[subscription-1][i][1] + '\n'
            message = '您訂閱的類別有新貼文!' + addr
        lineNotifyMessage(token, message)
    elif len(categories[subscription-1]) > 8:
        for i in range(8):
            addr += categories[subscription-1][i][1] + '\n'
            message = '您訂閱的類別有新貼文!' + addr
        lineNotifyMessage(token, message)
        for s in range(8, 16):
            addr1 += categories[subscription-1][i][1] + '\n'
            message1 = '您訂閱的類別有新貼文!' + addr1
        lineNotifyMessage(token, message1)
elif len(categories[subscription-1]) == 0:
    message = '沒有東西'
    lineNotifyMessage(token, message)

