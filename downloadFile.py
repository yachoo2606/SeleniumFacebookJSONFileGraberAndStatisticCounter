import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from time import sleep

load_dotenv()


def startDownload(driver, index):
    downloadDiv = driver.find_elements(By.CLASS_NAME,
                                       "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r"
                                       ".x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg"
                                       ".xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619"
                                       ".x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3")

    downloadDiv[1].click()

    # CLICK ON ITERATE ELEMENT

    filesDirs = driver.find_elements(By.CLASS_NAME,
                                     "x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x"
                                     ".x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xk50ysn.xzsf02u"
                                     ".x1yc453h")
    print(filesDirs)
    print(filesDirs[index].get_attribute("innerHTML"))
    sleep(2)
    filesDirs[index].click()
    sleep(7)


def downloadFiles():
    # SETUP SECTION

    options = Options()

    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", os.getcwd())
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.facebook.com/settings/?tab=your_facebook_information")
    driver.maximize_window()
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        print(button.get_attribute('title'))
        if button.get_attribute('title') == 'Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie':
            button.click()

    # LOGIN SECTION

    inputs = driver.find_elements(By.TAG_NAME, "input")

    for pageInput in inputs:

        if pageInput.get_attribute("name") == "email":
            pageInput.send_keys(os.environ.get("FBLOGIN"))

        if pageInput.get_attribute("name") == "pass":
            pageInput.send_keys(os.environ.get("FBPASSWD"))

    loginButton = driver.find_element(By.ID, "loginbutton")
    loginButton.click()

    # AFTER LOGIN SECTION

    WebDriverWait(driver, timeout=20).until(
        # )
        lambda d:
        d.current_url == "https://www.facebook.com/settings/?tab=your_facebook_information" and
        EC.presence_of_element_located(
            (By.XPATH, "//*[text()='Pobierz kopię informacji w celu zachowania lub przeniesienia do innej usługi.']"))
    )

    driver.get("https://www.facebook.com/dyi/?referrer=yfi_settings")

    # sleep(10)

    WebDriverWait(driver, timeout=20).until(
        lambda d:
        d.current_url == "https://www.facebook.com/dyi/?referrer=yfi_settings" and
        EC.presence_of_element_located((By.CLASS_NAME,
                                        "x1i10hfl.x6umtig.x1b1mbwd.xaqea5y.xav7gou.xe8uvvx.xggy1nq.x1o1ewxj.x3x9cwd"
                                        ".x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.xjbqb8w.x18o3ruo"
                                        ".x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619"
                                        ".x1heor9g.x1ypdohk.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69"
                                        ".xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1vjfegm.x3nfvp2.xrbpyxo.xng8ra.x16dsc37"))
    )

    # sleep(4)

    tabsButtons = driver.find_elements(By.CLASS_NAME,
                                       "x1i10hfl.x6umtig.x1b1mbwd.xaqea5y.xav7gou.xe8uvvx.xggy1nq.x1o1ewxj.x3x9cwd"
                                       ".x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.xjbqb8w.x18o3ruo"
                                       ".x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619"
                                       ".x1heor9g.x1ypdohk.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69"
                                       ".xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1vjfegm.x3nfvp2.xrbpyxo.xng8ra.x16dsc37")

    print(tabsButtons)

    for button in tabsButtons:
        if button.find_element(By.XPATH, "//*[text()='Dostępne pliki']"):
            button.click()

    # sleep(4)

    downloadDiv = driver.find_elements(By.CLASS_NAME,
                                       "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r"
                                       ".x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg"
                                       ".xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619"
                                       ".x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3")

    print(downloadDiv)
    downloadDiv[1].click()

    filesDirs = driver.find_elements(By.CLASS_NAME,
                                     "x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x"
                                     ".x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xk50ysn.xzsf02u"
                                     ".x1yc453h")

    print(len(filesDirs))
    downloadDiv[1].click()

    index = 14

    while index < len(filesDirs):

        found = False

        for file in os.listdir(os.getcwd()):
            if file.find("part") != -1:
                print("Downloading detected")
                found = True
                break

        if found:
            sleep(10)
            continue

        startDownload(driver, index)
        index += 1
        sleep(1)

    # driver.quit()


if __name__ == '__main__':
    downloadFiles()
