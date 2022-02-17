# 參閱7-28頁

import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials as sac
from datetime import datetime

from selenium import webdriver
import xlwt





from selenium.webdriver.chrome.options import Options 
chrome_options = webdriver.ChromeOptions() 
prefs = {"profile.default_content_setting_values.notifications" : 2} #關閉chrome通知
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('headless') #隱藏

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')


driver_path = 'C:\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome(driver_path,chrome_options=chrome_options)

url = 'https://sale.591.com.tw/?shType=list&regionid=6&section=75,67,73,76,68&shape=2&pattern=2,3&order=posttime_desc&area=20_30,30_40&houseage=$_17$&direction=4,3,1'
# https://sale.591.com.tw/?shType=list&regionid=6&section=75,67,73,76,68&shape=2&pattern=2,3&order=posttime_desc&area=20_30,30_40&houseage=$_17$&direction=4,3,1

driver.implicitly_wait(5) #預設載入最常等待時間
driver.get(url)
name = driver.find_elements_by_xpath("//div[contains(@class,'houseList-item-title')]/a")
style = driver.find_elements_by_xpath("//span[contains(@class,'houseList-item-attrs-layout')]")
section = driver.find_elements_by_xpath("//span[contains(@class,'houseList-item-section')]")
address = driver.find_elements_by_xpath("//span[contains(@class,'houseList-item-address')]")
price = driver.find_elements_by_xpath("//div[contains(@class,'houseList-item-price')]")



scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# 建立憑證
cr = sac.from_json_keyfile_name('google_auth.json', scope)  # 請自行修改檔名
gs = gspread.authorize(cr)

sh = gs.open('桃園房市')  # 請自行修改試算表名稱
# wks = sh.sheet1
wks = sh.worksheet('591觀察房')

# wks.update_acell('D2', 'swf.com.tw')
# wks.update_cell(2, 5, 'swf.com.tw')
wks.clear() #清掉舊的資料
now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
values = ['案件標題', '總價', '區域', '大約地點', '更新時間: '+now]
wks.insert_row(values, 1)
# wks.resize(1)

# print(name[0].text)
# wks.update_acell('A2',name[0].text)


for col in range(len(name)-1):    
    wks.update_cell(col+2,1,name[col].text)
    wks.update_cell(col+2,2,style[col].text)
    wks.update_cell(col+2,3,price[col].text)
    wks.update_cell(col+2,4,section[col].text)
    wks.update_cell(col+2,5,address[col].text)

    if col%10==0 and col!=0:
        time.sleep(60)
    