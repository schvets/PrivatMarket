from selenium import webdriver
from operator import is_not
from functools import partial

driver = webdriver.Firefox()
driver.get("https://privatmarket.ua/")
urls = set()
list_links = driver.find_elements_by_tag_name('a')

for i in list_links:
    urls.add(i.get_attribute('href'))

urls_none = filter(partial(is_not, None), urls)
valid_urls = [k for k in urls_none if 'https://' in k ]

v = (0, 0)
(passed, failed) = v

for i in valid_urls :
        driver2 = webdriver.Firefox()
        driver2.get(i)
        driver.implicitly_wait(90)

        try:
            if driver2.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div/div/a/img').is_displayed() and  driver2.find_element_by_xpath('/html/body/div[1]/footer/div/div/div[1]/div/a/img').is_displayed():
                driver2.quit()
                passed += 1
        except:
            failed += 1
            print("test failed outer url " + driver2.current_url)
            driver2.quit()
print ("URLs failed " + str(failed))
print ("URLs passed " + str(passed))
driver.quit()

