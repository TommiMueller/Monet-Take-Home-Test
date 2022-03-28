from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'C:\Users\Thoma\Downloads\chromedriver_win32\chromedriver.exe')
browser.get('https://google.com')
browser.maximize_window()
browser.implicitly_wait(5)


cookies_button = browser.find_element_by_xpath('//*[@id="L2AGLb"]/div')
cookies_button.click()


names = ['Amazon',
         'Asos',
         'H&M',
         'MediaMarkt',
         'Saturn',
         'Zalando',
         'ZARA',
         'Ansons']

for name in names:
    print(name)
    searchbar = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    searchbar.click()
    searchbar.send_keys(name +
                        ' Ratenzahlung',
                        Keys.ENTER)
    
    first_result = browser.find_element_by_class_name("DKV0Md")
    print(first_result.text)
    first_result.click()
    print(browser.current_url)
  
    browser.back()
    browser.back()


browser.quit()




