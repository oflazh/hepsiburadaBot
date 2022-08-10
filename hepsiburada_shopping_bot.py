#seleniumu kurdum "pip install selenium"
#chrome driver indirdim chrome'da çalışacağım için

from selenium import webdriver                               #seleniumu import ettik
from selenium.webdriver.chrome.options import Options         #
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select #dropdown list için
import pandas as pd
import numpy


option1 = Options()
option1.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", chrome_options=option1)
url = "https://www.hepsiburada.com/"                    #gideceğimiz urlyi yazdık
driver.get(url)                                     #url'ye gittik
driver.maximize_window()                            #sayfayı tam ekran yaptık
time.sleep(1)

df = pd.read_excel('trendy.xlsx', index_col=None, header=None)
sl = df.to_numpy()



def hepsiburada():
    search_bar = driver.find_element("xpath",'//*[@id="SearchBoxOld"]/div/div/div[1]/div[2]/input')
    search_bar.clear()
    search_bar.send_keys(sl[i])
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)
    try:
        if driver.find_element("class",'no-result-view-icon'):
            time.sleep(2)
            driver.get("https://checkout.hepsiburada.com/sepetim")
        pass
    except:
        driver.find_element("css_selector",
            "#VariantList\.VariantListing\.DiscountRate > div > div > div > div > div > div > div > div > div.toggleContent-switch").click()  # indirimli ürünler
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='SortingBox']/div/div/div/div/div[1]/div/label").click()  # sıralama seç
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='SortingBox']/div/div/div/div/div[2]/div/div[1]/a[4]/label/div").click()  # çok değernlendirilenler

        time.sleep(2)
        driver.find_element_by_id("i0").click()
        # ürüne tıkla
        time.sleep(1)
        tab1 = driver.window_handles[0]  # sekmeler arası geçiş
        tab2 = driver.window_handles[1]
        driver.close()  # close new tab
        driver.switch_to.window(tab2)
        time.sleep(1)
        sepeteekle = driver.find_element_by_id("addToCart")  # sepete ekle
        sepeteekle.click()
        time.sleep(1)
        driver.get("https://hepsiburada.com/")


for i in range(0,7):

    hepsiburada()
