

from selenium import webdriver
import xlwt
from datetime import datetime


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

wb = xlwt.Workbook()
ws = wb.add_sheet('591')

for col in range(len(name)-1):    
    ws.write(col,0,name[col].text)
    ws.write(col,1,style[col].text)
    ws.write(col,2,price[col].text)
    ws.write(col,3,section[col].text)
    ws.write(col,4,address[col].text)
    
wb.save('519爬蟲結果.xls')

driver.quit()