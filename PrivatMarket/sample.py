from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://python.org/")
list_links = driver.find_elements_by_tag_name('a')

for i in list_links:
        print (i.get_attribute('href'))

#driver.quit()