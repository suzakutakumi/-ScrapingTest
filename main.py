from selenium import webdriver
import time,sys

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome("C:\\Users\\suzak\\Downloads\\chromedriver_win32\\chromedriver.exe", options=options)

driver.get("https://www.clubdam.com/karaokesearch/?keyword=%s&type=keyword"%sys.argv[1])
time.sleep(2)
elements=driver.find_elements_by_xpath("//*[@class='song-name']/a")
data=[]
for e in elements:
    data.append(e.text)
driver.close()
if len(data)==0:
    print("Not Found")
else:
    print("%sで検索"%sys.argv[1])
    for e in data:
        print(e)