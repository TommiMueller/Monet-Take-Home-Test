# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# Google in Chrome öffnen
browser = webdriver.Chrome(r'C:\Users\Thoma\Downloads\chromedriver_win32\chromedriver.exe')
browser.get('https://google.com')
browser.maximize_window()

# Cookies akzeptieren
cookies_button = browser.find_element_by_xpath('//*[@id="L2AGLb"]/div')
cookies_button.click()



## Suchleiste
searchbar = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbar.click()
searchbar.send_keys('Amazon Ratenzahlung', Keys.ENTER)

## Suchergebnis
first_result = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/a/h3')
print(first_result.text)
first_result.click()
print(browser.current_url)


# Browser schließen
browser.quit()





## Fragen:
    #Brauche ich explicit waits?
    #Brauche ich DataFrame?
